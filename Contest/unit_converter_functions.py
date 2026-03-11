from force_resultant_calculator_functions import validate_magnitude as validate

def feet():
    meters = validate("Please enter the length(m): ")
    print(f"{meters:.2f} meters is equal to {meters *3.28084 :.2f} feet.")
    
def meters():
    feet = validate("Please enter the length in feet: ")
    print(f"{feet:.2f} feet is equal to {feet * 0.3048:.2f} meters.")

def pounds():
    kilograms = validate("Please enter the mass in kilograms: ")
    print(f"{kilograms:.2f} kilograms is equal to {kilograms * 2.20462:.2f} pounds.")

def kilograms():
    pounds = validate("Please enter the mass in pounds: ")
    print(f"{pounds:.2f} pounds is equal to {pounds * 0.453592:.2f} kilograms.")

def minutes():
    seconds = validate("Please enter the time in seconds: ")
    print(f"{seconds:.2f} seconds is equal to {seconds / 60:.2f} minutes.")

def seconds():
    minutes = validate("Please enter the time in minutes: ")
    print(f"{minutes:.2f} minutes is equal to {minutes * 60:.2f} seconds.")

def fahrenheit():
    celsius = validate("Please enter the temperature in degrees Celsius: ")
    print(f"{celsius:.2f}°C is equal to {(celsius*9/5) + 32:.2f}°F.")

def celsius():
    fahrenheit = validate("Please enter the temperature in degrees Fahrenheit: ")
    print(f"{fahrenheit:.2f}°F is equal to {(fahrenheit-32) * 5/9:.2f}°C.")

def kilometers_per_hour():
    ms = validate("Please enter the speed in meters per second: ")
    print(f"{ms:.2f} meters per second is equal to {ms * 3.6:.2f} kilometers per hour.")

def meters_per_second():
    kmh = validate("Please enter the speed in kilometers per hour: ")
    print(f"{kmh:.2f} kilometers per hour is equal to {kmh/3.6:.2f} meters per second.")