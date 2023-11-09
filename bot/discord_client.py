import discord

class DiscordBotClient(discord.Client):
    """Client to interact with the Discord API and process events."""
    
    def __init__(self, context_manager, mood_manager, relationship_manager, openai_client, rcon_client, config_manager, usage_logger, *args, **kwargs):
        """Initialize the Discord bot client with context, mood, relationship managers, OpenAI client, and RCON client."""
        super().__init__(*args, **kwargs)
        self.context_manager = context_manager
        self.mood_manager = mood_manager
        self.relationship_manager = relationship_manager
        self.openai_client = openai_client
        self.rcon_client = rcon_client
        self.config_manager = config_manager
        self.usage_logger = usage_logger
    

    async def on_ready(self):
        """Called when the bot is ready to start."""
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    

    async def on_message(self, message):
        """Called when a message is sent to a channel the bot is in."""
        # Check if the bot is mentioned
        bot_mention = f'<@{self.user.id}>'
        role_mention = f'<@&{self.user.id}>'
        response = None
        current_config = self.config_manager.get_current_config()['api_type']
        # Don't respond to messages from the bot itself
        # NOTE: These should still be logged in the thread
        if message.author.id == self.user.id:
            return
        if message.content.startswith('<CONFIG>'):
            await self.__change_openai_config(message)
            return
        if bot_mention in message.content or role_mention in message.content:
            # Get response and log everything
            response = await self.openai_client.generate_response(message, current_config)
        if response is not None:
            await message.channel.send(response.choices[0].message.content)
            self.usage_logger.log_usage(
                prompt_timestamp=message.created_at.isoformat(),
                server_name=message.guild.name,
                server_id=str(message.guild.id),
                channel_name=message.channel.name,
                user_name=message.author.name,
                user_id=str(message.author.id),
                config_name=current_config,
                prompt=message.content,
                response=response.choices[0].message.content,
                prompt_tokens=str(response.usage.prompt_tokens),
                completion_tokens=str(response.usage.completion_tokens),
                total_tokens=str(response.usage.total_tokens),
                message_id=str(message.id),
                response_time="NOT IMPLEMENTED",
                bot_mood="NOT IMPLEMENTED",
                interaction_type='Mention' if bot_mention in message.content else 'Role Mention',
                cost_info="NOT IMPLEMENTED"
            )


    async def on_member_join(self, member):
        """Handle the event when a new member joins a server."""
        pass
    

    async def on_member_remove(self, member):
        """Handle the event when a member leaves a server."""
        pass


    ####################
    # HELPER FUNCTIONS #
    ####################


    async def __change_openai_config(self, message):
        # if not message.author.guild_permissions.administrator and not message.author.guild_permissions.manage_guild:
        if message.author.id != 97130788482449408:
            # await message.channel.send(f"{message.author.name} does not have sufficient rights to invoke <CONFIG>.")
            await message.channel.send(f"You are not the creator of Steve!")
            return
        parts = message.content.split()
        if len(parts) < 2:
            configs = self.config_manager.list_configs()
            configs_string = '\n'.join(f"{index + 1}. <CONFIG> {config}" for index, config in enumerate(configs))
            await message.channel.send(f"**Current Config: **{self.config_manager.get_current_config()['api_type']}\n*Please specify a configuration for OpenAI implementation:*\n{configs_string}")
            return
        new_config = parts[1]
        if self.config_manager.set_config(new_config):
            await message.channel.send(f"Configuration changed to {new_config}.")
        else:
            await message.channel.send(f"Unknown configuration: {new_config}")