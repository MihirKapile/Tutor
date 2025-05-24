import operator
from agno.tools import tool

@tool
def calculate(expression: str) -> str:
    """Performs a basic arithmetic calculation given an expression string (e.g., "2 + 3", "15 * 3").
    Supports addition, subtraction, multiplication, and division.
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error performing calculation: {e}"