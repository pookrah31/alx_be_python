FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


try:
    temperature = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
      converted_temp = convert_to_celsius(temperature)
      print(f"{temperature}℉ is equal to {converted_temp:.2f}℃")
    elif unit == "C":
      converted_temp = convert_to_fahrenheit(temperature)
      print(f"{temperature}℃ is equal to {converted_temp:.2f}℉")
    else:
      print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value")