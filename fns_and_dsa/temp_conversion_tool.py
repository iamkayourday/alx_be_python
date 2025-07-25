# Temperature Conversion Tool

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to celsius
    # C = (F - 32) x 5/9
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    # F = (C × 9/5) + 32
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("")
    print("**********Temperature Conversion Tool**********")
    temp = float(input("Enter the temperature to convert: "))    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is equal to {converted_temp}°C")
    else:
        print(f"Invalid unit '{unit}'. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

main()


