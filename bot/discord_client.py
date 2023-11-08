import discord

class DiscordBotClient(discord.Client):
    """Client to interact with the Discord API and process events."""
    
    def __init__(self, context_manager, mood_manager, relationship_manager, openai_client, rcon_client, config_manager, *args, **kwargs):
        """Initialize the Discord bot client with context, mood, relationship managers, OpenAI client, and RCON client."""
        super().__init__(*args, **kwargs)
        self.context_manager = context_manager
        self.mood_manager = mood_manager
        self.relationship_manager = relationship_manager
        self.openai_client = openai_client
        self.rcon_client = rcon_client
        self.config_manager = config_manager
    
    async def on_ready(self):
        """Called when the bot is ready to start."""
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
    
    async def on_message(self, message):
        """Called when a message is sent to a channel the bot is in."""
        # Don't respond to messages from the bot itself
        # NOTE: These should still be logged in the thread
        if message.author.id == self.user.id:
            return

        if message.content.startswith('<CONFIG>'):
            change_openai_config(self, message)

        
    
    async def on_member_join(self, member):
        """Handle the event when a new member joins a server."""
        pass
    
    async def on_member_remove(self, member):
        """Handle the event when a member leaves a server."""
        pass

    ####################
    # HELPER FUNCTIONS #
    ####################

    def change_openai_config(self, message):
        if not message.author.guild_permissions.administrator and not message.author.guild_permissions.manage_guild:
            await message.channel.send(f"{message.author.name} does not have sufficient rights to invoke <CONFIG>.")
            return
        parts = message.content.split()
        if len(parts) < 2:
            configs_string = '\n'.join(f"{index + 1}. <CONFIG> {config}" for index, config in self.config_manager.list_configs())
            await message.channel.send(f"*Please specify a configuration for OpenAI implementation:*{configs_string}")
            return
        new_config = parts[1]
        if self.config_manager.set_config(new_config):
            await message.channel.send(f"Configuration changed to {new_config}.")
        else:
            await message.channel.send(f"Unknown configuration: {new_config}")