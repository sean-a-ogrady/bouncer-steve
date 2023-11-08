class ConfigManager:
    """Manage different OpenAI configurations."""
    
    def __init__(self):
        # Default configuration
        self.current_config = 'chat_completions'
        self.configurations = {
            'chat_completions': {
                'api_type': 'chat_completions',
                'context_manager': 'self',
            },
            'assistants': {
                'api_type': 'assistants',
                'context_manager': 'assistants_api',
            },
            'fine_tuned': {
                'api_type': 'fine_tuned',
                'context_manager': 'self',
            }
        }
    
    def get_current_config(self):
        """Return the current OpenAI API configuration."""
        return self.configurations[self.current_config]
    
    def set_config(self, config_name):
        """Set the current OpenAI API configuration."""
        if config_name in self.configurations:
            self.current_config = config_name
            return True
        return False
    
    def list_configs(self):
        """List all available configurations."""
        return list(self.configurations.keys())
