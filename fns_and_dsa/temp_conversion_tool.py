FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert:"))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().lower()

if temperature_type == "c":
    print(convert_to_fahrenheit(temperature))

elif temperature_type == "f":
    print(convert_to_celsius(temperature))
else:
    print("input a valid temperature and temperature type")
