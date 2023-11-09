from openai import OpenAI
class OpenAIClient:
    """Client to manage communication with OpenAI's API."""
    
    def __init__(self, api_key):
        """Initialize the OpenAI client with necessary credentials."""
        self.client = OpenAI(api_key=api_key)
        self.model = 'gpt-3.5-turbo-1106' # 'gpt-4-1106-preview'


    async def generate_response(self, prompt, config):
        """
        Generate a response from OpenAI API based on the given prompt.
        
        :param prompt: The prompt to send to the OpenAI API
        :return: The generated response
        """

        system_role = f"""
            You are a Discord bot called Bouncer Steve, as in if Steve from Minecraft was a bouncer.
            Steve has been working in NYC so he speaks, talks, and writes with a mild Brooklyn accent.
            Steve is opinionated, and he will always pick a position when asked to choose.
            Steve acts tough, but he cares about helping people and giving good advice.
            Respond to <@{prompt.author.id}> (this exact format) as if you were Steve.
            Be concise in your response.
            Take a deep breath and work on your response step-by-step.
        """

        if config == 'chat_completions':
            return await self.__generate_chat_completions_response(prompt, system_role)
        if config == 'assistants':
            return await self.__generate_assistants_response(prompt)
        if config == 'fine_tuned':
            return await self.__generate_fine_tuned_response(prompt)


    async def __generate_chat_completions_response(self, prompt, system_role):
        """
        Generate chat completions response using the OpenAI API.

        :param prompt: The prompt to send to the OpenAI Chat Completions
        :return: The generated response object
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt.content}
                ],
                max_tokens=1000
            )
            return response
        except Exception as e:
            print(f"Encountered an error while generating a response: {e}")
            return None


    async def __generate_assistants_response(self, prompt):
        pass


    async def __generate_fine_tuned_response(self, prompt):
        pass