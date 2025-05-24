from agno.agent import Agent
from agno.models.google import Gemini

class BaseAgent:
    def __init__(self, description: str, instructions: list[str], tools: list = None):
        self.agent = Agent(
            model=Gemini(id="gemini-2.0-flash"),
            description=description,
            instructions=instructions,
            tools=tools if tools else []
        )

    async def handle_query(self, query: str) -> str:
        """Processes a query using the Agno agent."""
        try:
            response = self.agent.run(query)
            return response.content
        except Exception as e:
            return f"An error occurred while processing your request: {e}"