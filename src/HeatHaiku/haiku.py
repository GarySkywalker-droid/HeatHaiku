import random
from typing import List


def generate_haiku(temperature: float) -> str:
    """
    Generate a haiku based on CPU temperature.

    Args:
        temperature: CPU temperature in Celsius

    Returns:
        A beautiful 5-7-5 syllable haiku string
    """
    temp_range = _get_temperature_range(temperature)
    haiku_templates = _get_haiku_templates(temp_range)

    # Select a random haiku template
    template = random.choice(haiku_templates)

    # Format with temperature
    return template.format(temp=int(temperature))


def _get_temperature_range(temperature: float) -> str:
    """Categorize temperature into ranges."""
    if temperature < 40:
        return "cold"
    elif temperature < 60:
        return "warm"
    elif temperature < 80:
        return "hot"
    else:
        return "critical"


def _get_haiku_templates(temp_range: str) -> List[str]:
    """Get haiku templates for temperature range."""
    templates = {
        "cold": [
            "Silicon sleeps deep\nCool circuits whisper softly\nWinter in the core",
            "Frost on the CPU\nQuiet processing power\nIce dreams in the chip",
            "Cold metal resting\nBits flow like gentle snowfall\nPeace in every core",
            "Frozen calculations\nSilent streams of data flow\nWinter's gentle hum",
        ],
        "warm": [
            "Warm circuits awakening\nSpring flows through silicon paths\nLife in every bit",
            "Gentle heat rising\nProcessors dance with the sun\nBalance in the core",
            "Comfortable warmth spreads\nThrough pathways of pure logic\nHarmony blooms bright",
            "Mild temperature\nLike morning coffee brewing\nReady for the day",
        ],
        "hot": [
            "Fire in the circuits\nPower surges through each core\nSummer's fierce embrace",
            "Heat waves dance on chips\nIntense calculations burn\nPassion in each volt",
            "Blazing silicon\nEnergy flows like lava\nThe CPU burns bright",
            "Desert heat within\nProcessors work overtime\nFire feeds the code",
        ],
        "critical": [
            "Volcano awakens!\nDanger signals flash red hot\nCooling fans cry out",
            "Critical alert!\nMolten silicon screams hot\nThrottling kicks in now",
            "Emergency heat!\nThe processor begs for air\nSave me from this fire",
            "Warning: {temp} degrees!\nThermal limits pushed too far\nShutdown imminent",
        ],
    }

    return templates.get(temp_range, templates["warm"])


def get_temperature_emoji(temperature: float) -> str:
    """Get emoji representing temperature range."""
    if temperature < 40:
        return "❄️"
    elif temperature < 60:
        return "🌡️"
    elif temperature < 80:
        return "🔥"
    else:
        return "🚨"


def format_haiku_display(temperature: float, haiku: str) -> str:
    """Format haiku for a beautiful display."""
    emoji = get_temperature_emoji(temperature)
    temp_str = f"{temperature:.1f}°C"

    return f"""
{emoji} CPU Temperature: {temp_str} {emoji}

🎋 Your Thermal Haiku:

{haiku}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
