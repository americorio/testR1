def convert_to_fahrenheit(celsius):
    #Convert a temperature from Celsius to Fahrenheit.
    #Formula: F = C * 9/5 + 32
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

print(convert_to_fahrenheit(0))    # Expect 32.0
print(convert_to_fahrenheit(100))  # Expect 212.0
