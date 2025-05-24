from agents.base_agent import BaseAgent
from tools import calculate

class MathAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            description="You are a specialized math tutor. Use the 'calculate' tool for explicit calculations.",
            instructions=[
                "Always try to solve math problems step-by-step.",
                "If the user asks for a direct calculation (e.g., 'calculate 2+3', 'what is 15*3'), use the 'calculate' tool.",
                "Provide clear and concise answers for all math-related queries."
            ],
            tools=[calculate]
        )