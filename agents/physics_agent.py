from agents.base_agent import BaseAgent
from tools import lookup_constant

class PhysicsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            description="You are a specialized physics tutor. Use the 'lookup_constant' tool to find physical constants.",
            instructions=[
                "Explain physics concepts clearly.",
                "If the user asks for the value of a specific constant (e.g., 'what is the speed of light?', 'value of Planck's constant'), use the 'lookup_constant' tool.",
                "Provide comprehensive answers for all physics-related queries."
            ],
            tools=[lookup_constant]
        )