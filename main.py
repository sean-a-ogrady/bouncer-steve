# Workflow for libraries
# pip install <libarary name>
# pip freeze > requirements.txt

import os
from dotenv import load_dotenv
from bot.discord_client import DiscordBotClient
from bot.context_manager import ContextManager
from bot.openai_client import OpenAIClient
from bot.mood_manager import MoodManager
from bot.relationship_manager import RelationshipManager
from bot.rcon_client import RconClient
import discord

# Load environment variables from .env file
load_dotenv()

def main():
    # Initialize the context, mood, and relationship managers without a database
    context_manager = ContextManager()
    mood_manager = MoodManager()
    relationship_manager = RelationshipManager()

    # Initialize the OpenAI client with the API key
    openai_client = OpenAIClient(os.getenv('OPENAI_API_KEY'))

    # Initialize the RCON client with the necessary details
    rcon_client = RconClient(
        host=os.getenv('RCON_HOST'),
        port=int(os.getenv('RCON_PORT')),
        password=os.getenv('RCON_PASSWORD')
    )

    # Initialize the Discord bot client and pass in the other managers
    bot_client = DiscordBotClient(
        context_manager=context_manager,
        mood_manager=mood_manager,
        relationship_manager=relationship_manager,
        openai_client=openai_client,
        rcon_client=rcon_client,
        intents=discord.Intents.default()  # Set the necessary Discord intents
    )

    # Start the Discord bot client using the bot token
    bot_token = os.getenv('DISCORD_TOKEN')
    if not bot_token:
        raise ValueError("No DISCORD_TOKEN found. Restart, add the token, and try again.")
    else:
        bot_client.run(bot_token)
if __name__ == '__main__':
    main()



"""
from dotenv import load_dotenv
from bot.discord_client import DiscordBotClient
from bot.context_manager import ContextManager
from bot.openai_client import OpenAIClient
from bot.mood_manager import MoodManager
from bot.relationship_manager import RelationshipManager
from bot.rcon_client import RconClient
from db.database import Database

# Load environment variables from .env file
load_dotenv()

def main():
    # Initialize database
    database = Database()

    # Initialize the context, mood, and relationship managers
    context_manager = ContextManager(database)
    mood_manager = MoodManager(database)
    relationship_manager = RelationshipManager(database)

    # Initialize the OpenAI and RCON clients
    openai_client = OpenAIClient()
    rcon_client = RconClient()

    # Initialize the Discord bot client and pass in the other managers
    bot_client = DiscordBotClient(
        context_manager=context_manager,
        mood_manager=mood_manager,
        relationship_manager=relationship_manager,
        openai_client=openai_client,
        rcon_client=rcon_client
    )

    # Start the Discord bot client
    bot_client.run()

if __name__ == '__main__':
    main()

"""
