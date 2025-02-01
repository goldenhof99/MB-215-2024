def convert_temperature(temp, unit):
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        temp (float): The temperature value.
        unit (str): 'C' for Celsius or 'F' for Fahrenheit.

    Returns:
        float: The converted temperature.
    """
    if unit.lower() == 'c':
        return (temp * 9/5) + 32  # Convert Celsius to Fahrenheit
    elif unit.lower() == 'f':
        return (temp - 32) * 5/9  # Convert Fahrenheit to Celsius
    else:
        return "Invalid unit! Use 'C' for Celsius or 'F' for Fahrenheit."

# Test the code
if __name__ == "__main__":
    print(f"Converting 100F to Celsius: {convert_temperature(100, 'F'):.2f}")
    print(f"Converting 0C to Fahrenheit: {convert_temperature(0, 'C'):.2f}")
