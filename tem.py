def categorize_temperature(temp_c):
    """
    Categorize temperature in Celsius.
    Adjust thresholds as needed.
    """
    if temp_c <= 15:
        return "Cold"
    elif temp_c <= 25:
        return "Normal"
    else:
        return "Hot"

def get_temperature_and_unit():
    """
    Returns (temperature_value, unit) where unit is 'C' or 'F'.
    """
    while True:
        s = input("Enter temperature with unit (e.g. 25 C or 77 F): ")
        parts = s.strip().split()
        if len(parts) != 2:
            print("Please enter in format: <number> <unit> (C or F).")
            continue
        num_str, unit = parts
        unit = unit.upper()
        if unit not in ("C", "F"):
            print("Unit must be 'C' or 'F'. Try again.")
            continue
        try:
            val = float(num_str)
        except ValueError:
            print("Could not parse the number. Try again.")
            continue
        return val, unit

def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(c):
    return c * 9.0 / 5.0 + 32

def main():
    print("Temperature categorization (accepts C or F)")

    val, unit = get_temperature_and_unit()
    if unit == "F":
        temp_c = fahrenheit_to_celsius(val)
        print(f"Converted: {val:.2f} °F → {temp_c:.2f} °C")
    else:
        temp_c = val

    category = categorize_temperature(temp_c)
    temp_f_converted = celsius_to_fahrenheit(temp_c)

    print(f"Final: {temp_c:.2f} °C → Category: {category}")
    print(f"In Fahrenheit: {temp_f_converted:.2f} °F")

if __name__ == "__main__":
    main()
