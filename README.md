# Bouncer Steve

![](https://cdn.discordapp.com/attachments/335080098715795456/1172616570380505118/image.png?ex=6560f748&is=654e8248&hm=a3c3b2cf839c4c525843ad93346f109504b5c85e213430eb24c1cc33f30e54e8&)

Introducing Bouncer Steve, the virtual bouncer of your Discord server! Steve from Minecraft has since hung up his pickaxe and has started moonlighting as your personal digital bouncer. He's a friendly yet firm presence in your server who's always ready to lend a helping hand or drop some words of wisdom, all with a mild Brooklyn accent.

## What Does Steve Do?
Bouncer Steve isn't just any bot. He's the bot you want on your side when things get dicey in the digital world. Whether you need advice or someone to interface with your Minecraft server's console without breaking a sweat, Steve's your guy. All you need to do is give him a mention (@Bouncer Steve), and he'll come running ready to chat, engage, and bring a smile to your server's face.

Beneath that pixelated exterior beats the heart of a bot who cares — Steve's always looking to make a connection, engage in conversation, and remember what makes each member of your server tick.

## Ready to Get Started?
Steve is currently in alpha, so the following instructions won't be needed in the upcoming release. Below you'll find all the details you need to get Bouncer Steve up and running in your Discord server. Follow along, and let the fun begin!

## Project Directory Hierarchy

```bash
bouncer-steve/
│
├── bot/                                 # Bot-related code
│   ├── config_manager.py                # Manages different configurations
│   ├── context_manager.py               # Manages conversation context
│   ├── discord_client.py                # Discord client handling events and commands
│   ├── mood_manager.py                  # Manages the bot's mood
│   ├── openai_client.py                 # Interfaces with the OpenAI API
│   ├── rcon_client.py                   # Handles RCON connections for Minecraft
│   └── relationship_manager.py          # Manages relationships with users
│   └── usage_logger.py                  # Logs usage data
│
├── db/                                  # Database-related code
│
├── logs/                                # Directory for log files
│
├── .env                                 # Environment variables (you have to set this up)
├── .gitignore                           # Specifies intentionally untracked files to ignore
├── Dockerfile                           # Docker container specification
├── main.py                              # Main entry point of the bot application
├── README.md                            # Project documentation
├── requirements.txt                     # Python dependencies
└── summary.md                           # Project summary documentation
```

## Installation

### Cloning the Repository

To get started with Bouncer Steve, you'll need to clone the repository from GitHub:

1. Open a terminal on your machine.
2. Clone the repository:

```bash
git clone https://github.com/sean-a-ogrady/bouncer-steve.git
```

3. Navigate into the cloned directory:

```bash
cd bouncer-steve
```

### Setting Up Environment Variables

You'll need to set up your environment variables with your Discord bot token and your OpenAI API key.

1. Create a Discord Bot and get your token:
    - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    - Click "New Application" and name it "Bouncer Steve".
    - Go to the "Bot" tab and click "Add Bot".
    - Uncheck "Public Bot", and check all of the Privileged Gateway Intents.
    - Click "Reset Token" and copy the new token.

2. Obtain your OpenAI API key:
    - Sign up or log in at [OpenAI](https://openai.com/).
    - Navigate to the [API keys page](https://platform.openai.com/api-keys).
    > **Note:** You need a ChatGPT Plus subscription for access to the API.
    - You may need to create a new API key if one isn't already available.
    - Copy the API key to use it in the next step.

3. In the root directory of the project, create a file named `.env`.

4. Inside the `.env` file, add your Discord bot token and OpenAI API key:

```plaintext
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_discord_bot_token_here` and `your_openai_api_key_here` with the actual tokens you obtained from the previous steps.

### Installing Dependencies

1. Ensure Python is installed on your system.
2. If using a virtual environment, activate it.
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Inviting Bouncer Steve to Your Server

Having Bouncer Steve join your Discord server is a simple process. Follow these steps to generate an invite link and bring Steve into your server community:

1. **Navigate to the Discord Developer Portal**:
   - Open your web browser and go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Log in with your Discord credentials if you're not already logged in.

2. **Access Your Application**:
   - Find the application for Bouncer Steve that you created earlier in the list of your applications.
   - Click on the application's name to open its settings.

3. **Create an OAuth2 Invite Link**:
   - Select the "OAuth2" tab from the left-hand menu.
   - Scroll down to the "OAuth2 URL Generator" section.
   - In the "SCOPES" section, check the box next to "bot" to indicate that you're inviting a bot to your server.

4. **Set Bot Permissions**:
   - Still within the "OAuth2 URL Generator" section, you'll find the "BOT PERMISSIONS" area below the "SCOPES" section.
   - Here, you need to specify what permissions Steve needs to function correctly. At a minimum, Bouncer Steve requires the following permissions:
     - **Send Messages**: Allows Steve to reply to users in text channels.
     - **Read Message History**: Enables Steve to understand the context of conversations.
   - Check the boxes next to these permissions. If Steve has more functionality, like managing roles or channels, you'll need to select those permissions as well.

5. **Generate the Invite Link**:
   - After selecting the appropriate scopes and permissions, an invite link will be automatically generated at the bottom of the "SCOPES" section.
   - Copy this invite link.

6. **Invite Steve to Your Server**:
   - Paste the invite link into your web browser's address bar and press Enter.
   - You'll be prompted to select the server to which you want to add Bouncer Steve.
   - Choose the desired server from the dropdown list (you must have the "Manage Server" permission on the server you select).
   - Click "Continue," and then "Authorize" after reviewing the requested permissions.
   - Complete any additional verification required by Discord.

And that's it! Bouncer Steve will now appear in the member list of your server, ready to engage with users and bring his unique flair to your community.

### Running the Bot

1. Start Bouncer Steve by running:

```bash
python main.py
```

2. Bouncer Steve should now be active in your Discord server!

## Feature Roadmap

- [x] Mention **@Bouncer Steve** in chat and he will respond!
- [ ] Interface with your Minecraft server's console through Steve for whitelist management
- [ ] Steve responds with context from the current conversation
- [ ] Steve remembers his past interactions with members of the server
- [ ] Steve has an internal mood state that affects his interactions
- [ ] More features to come! Reach out to me at ogrady.sean.a@gmail.com with feature requests!

## Credits

The **Bouncer Steve** bot project is created and maintained by [Sean O'Grady](https://sean-ogrady.com) (2023).