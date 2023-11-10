import csv
import os
from datetime import datetime

class UsageLogger:
    """Logs detailed usage of OpenAI configurations to a CSV file within a logs directory."""
    
    def __init__(self, csv_file='usage_log.csv'):
        self.logs_dir = 'logs'
        self.csv_file = os.path.join(self.logs_dir, csv_file)
        
        # Create logs directory if it doesn't exist
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Check if CSV file exists, if not, create it with the header
        if not os.path.isfile(self.csv_file):
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['prompt_timestamp', 'server_name', 'server_id', 'channel_name', 'user_name', 'user_id', 
                                 'config_name', 'openai_model', 'prompt', 'response', 'prompt_tokens', 'completion_tokens',
                                 'total_tokens', 'message_id', 'response_time', 'bot_mood',  'interaction_type', 'cost_info'])
                               
    def log_usage(self, server_name, server_id, channel_name, user_name, user_id, config_name, openai_model,
                  prompt, response, prompt_tokens, completion_tokens, total_tokens, message_id, response_time, bot_mood, 
                  prompt_timestamp, interaction_type, cost_info):
        """Log the usage of an OpenAI configuration with detailed server, channel, and user info."""
        log_entry = [
            prompt_timestamp,            # Timestamp of when the prompt was created
            server_name,                 # Name of the server where the interaction took place
            server_id,                   # ID of the server
            channel_name,                # Name of the channel where the interaction took place
            user_name,                   # Name of the user who interacted with the bot
            user_id,                     # ID of the user
            config_name,                 # Name of the OpenAI configuration used
            openai_model,                # The OpenAI model the bot is using
            prompt,                      # The prompt that was sent to the OpenAI API
            response,                    # The response received from the OpenAI API
            prompt_tokens,               # The number of tokens used by the OpenAI API for the prompt
            completion_tokens,           # The number of tokens used by the OpenAI API for the completion
            total_tokens,                # The total number of tokens used by the OpenAI API
            message_id,                  # ID of the message that triggered the bot's response
            response_time,               # Time taken by the bot to respond
            bot_mood,                    # Mood of the bot during the interaction
            interaction_type,            # Type of interaction (command, mention, etc.)
            cost_info                    # Cost information provided by the OpenAI API
        ]
        
        # Append the log entry to the CSV file
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(log_entry)
