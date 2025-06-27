from .temperature import get_cpu_temperature
from .haiku import generate_haiku, format_haiku_display


def main():
    """Entry point for the heathaikuu command."""
    print("🌡️  HeatHaiku - CPU Temperature Poetry Generator")
    print("📊 Monitoring CPU temperatures...")
    print("🎋 Generating thermal haikus...")
    temp = get_cpu_temperature()
    if temp is None:
        print("Unable to read CPU temperature.")
        return

    haiku = generate_haiku(temp)
    display = format_haiku_display(temp, haiku)

    print(display)


if __name__ == "__main__":
    main()
