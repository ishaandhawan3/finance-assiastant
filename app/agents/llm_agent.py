import ollama
from ollama import AsyncClient
from app.utils import log_ai_tool_usage

class LLMAgent:
    def __init__(self):
        self.client = AsyncClient()

    async def generate_brief(self, context: str) -> str:
        """Generate market brief using Mistral via Ollama"""
        try:
            response = await self.client.chat(
                model='mistral',
                messages=[{
                    'role': 'user',
                    'content': f"Generate a comprehensive market brief based on: {context}"
                }],
                stream=True
            )
            full_response = []
            async for chunk in response:
                if 'message' in chunk and 'content' in chunk['message']:
                    full_response.append(chunk['message']['content'])
            log_ai_tool_usage("Ollama", "Generated market brief")
            return ''.join(full_response)
        except Exception as e:
            log_ai_tool_usage("Ollama", f"Error: {str(e)}")
            return "Market analysis unavailable at this time"
