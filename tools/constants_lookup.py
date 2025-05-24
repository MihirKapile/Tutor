from agno.tools import tool

PHYSICS_CONSTANTS = {
    "speed of light": "299,792,458 m/s (c)",
    "gravitational constant": "6.674 × 10^-11 N(m/kg)^2 (G)",
    "planck's constant": "6.62607015 × 10^-34 J⋅s (h)",
    "electron charge": "1.602 × 10^-19 C (e)",
    "boltzmann constant": "1.380649 × 10^-23 J/K (k)",
    "avogadro's number": "6.022 × 10^23 mol^-1 (Na)"
}

@tool
def lookup_constant(constant_name: str) -> str:
    """Looks up the value of a common physics constant."""
    for key, value in PHYSICS_CONSTANTS.items():
        if constant_name.lower() in key:
            return f"The {key} is approximately {value}."
    return f"Sorry, I don't have information on '{constant_name}' in my constant database."