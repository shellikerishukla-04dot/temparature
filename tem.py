def categorize_temperature(temp_c):
    """
    Categorize temperature in Celsius:
     - “Cold” if below some threshold (e.g. < 15 °C)
     - “Normal” if in a middle range (e.g. 15-25 °C)
     - “Hot” if above some threshold (e.g. > 25 °C)
    You can adjust thresholds as needed.
    """
    if temp_c < 0 or temp_c > 1000:  # sanity check, adjust upper bound if needed
        return "Invalid temperature"
    if temp_c <= 15:
        return "Cold"
    elif temp_c <= 25:
        return "Normal"
    else:
        return "Hot"

def get_temperature_input():
    """
    Prompts user for temperature (in Celsius),
    validates input, returns float.
    """
    while True:
        s = input("Enter temperature (in °C): ")
        try:
            t = float(s)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        # You can impose some reasonable bounds
        # Let's accept −100 to 500 °C for example
        if t < -100 or t > 500:
            print("Temperature out of realistic range. Try again.")
            continue
        return t

def main():
    print("Temperature categorization")
    temp_c = get_temperature_input()
    category = categorize_temperature(temp_c)
    print(f"Temperature: {temp_c:.2f} °C → Category: {category}")

if __name__ == "__main__":
    main()
