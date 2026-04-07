import math
import numpy as np
import matplotlib.pyplot as plt

# Linear script - no separate functions
print("===== Welcome to Our Engineering Calculator! =====")

while True:
    print("\nMain Menu:")
    print("1. Force Resultant Calculator (2D)")
    print("2. Quadratic Equation Solver")
    print("3. Unit Converter")
    print("4. Quit")

    choice = input("Enter your choice: ")

    # ---------------- FORCE RESULTANT CALCULATOR ----------------
    if choice == "1":
        print("\n2D Force Resultant Calculator")
        try:
            F1x = float(input("Enter F1 x-component: "))
            F1y = float(input("Enter F1 y-component: "))
            F2x = float(input("Enter F2 x-component: "))
            F2y = float(input("Enter F2 y-component: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        # Calculate resultant
        Rx = F1x + F2x
        Ry = F1y + F2y
        magnitude = math.sqrt(Rx**2 + Ry**2)
        angle = math.degrees(math.atan2(Ry, Rx))
        print(f"Resultant Vector: Rx = {Rx}, Ry = {Ry}")
        print(f"Magnitude = {magnitude:.2f}, Angle = {angle:.2f}°")


    # ---------------- QUADRATIC EQUATION ----------------
    elif choice == "2":
        print("\nQuadratic Equation Solver (ax² + bx + c = 0)")
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Two real solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif discriminant == 0:
            x = -b / (2*a)
            print(f"One real solution: x = {x:.2f}")
        else:
            print("No real solutions.")

    # ---------------- UNIT CONVERTER ----------------
    elif choice == "3":
        while True:
            print("\nUnit Converter Menu:")
            print("1. Length (meters <-> feet)")
            print("2. Mass (kilograms <-> pounds)")
            print("3. Time (seconds <-> minutes)")
            print("4. Temperature (Celsius <-> Fahrenheit)")
            print("5. Speed (m/s <-> km/h)")
            print("6. Back to main menu")

            selection = input("Enter your choice: ")

            # -------- LENGTH --------
            if selection == "1":
                while True:
                    print("\nLength Conversion:")
                    print("1. meters -> feet")
                    print("2. feet -> meters")
                    print("3. Back")
                    conv = input("Choice: ")
                    if conv == "1":
                        meters = float(input("Enter meters: "))
                        print(f"{meters:.2f} m = {meters * 3.28084:.2f} ft")
                    elif conv == "2":
                        feet = float(input("Enter feet: "))
                        print(f"{feet:.2f} ft = {feet * 0.3048:.2f} m")
                    elif conv == "3":
                        break
                    else:
                        print("Invalid option. Please select 1-3.")

            # -------- MASS --------
            elif selection == "2":
                while True:
                    print("\nMass Conversion:")
                    print("1. kilograms -> pounds")
                    print("2. pounds -> kilograms")
                    print("3. Back")
                    conv = input("Choice: ")
                    if conv == "1":
                        kg = float(input("Enter kilograms: "))
                        print(f"{kg:.2f} kg = {kg * 2.20462:.2f} lbs")
                    elif conv == "2":
                        lbs = float(input("Enter pounds: "))
                        print(f"{lbs:.2f} lbs = {lbs * 0.453592:.2f} kg")
                    elif conv == "3":
                        break
                    else:
                        print("Invalid option. Please select 1-3.")

            # -------- TIME --------
            elif selection == "3":
                while True:
                    print("\nTime Conversion:")
                    print("1. seconds -> minutes")
                    print("2. minutes -> seconds")
                    print("3. Back")
                    conv = input("Choice: ")
                    if conv == "1":
                        sec = float(input("Enter seconds: "))
                        print(f"{sec:.2f} s = {sec / 60:.2f} min")
                    elif conv == "2":
                        mins = float(input("Enter minutes: "))
                        print(f"{mins:.2f} min = {mins * 60:.2f} s")
                    elif conv == "3":
                        break
                    else:
                        print("Invalid option. Please select 1-3.")

            # -------- TEMPERATURE --------
            elif selection == "4":
                while True:
                    print("\nTemperature Conversion:")
                    print("1. Celsius -> Fahrenheit")
                    print("2. Fahrenheit -> Celsius")
                    print("3. Back")
                    conv = input("Choice: ")
                    if conv == "1":
                        c = float(input("Enter °C: "))
                        print(f"{c:.2f} °C = {(c*9/5)+32:.2f} °F")
                    elif conv == "2":
                        f = float(input("Enter °F: "))
                        print(f"{f:.2f} °F = {(f-32)*5/9:.2f} °C")
                    elif conv == "3":
                        break
                    else:
                        print("Invalid option. Please select 1-3.")

            # -------- SPEED --------
            elif selection == "5":
                while True:
                    print("\nSpeed Conversion:")
                    print("1. m/s -> km/h")
                    print("2. km/h -> m/s")
                    print("3. Back")
                    conv = input("Choice: ")
                    if conv == "1":
                        ms = float(input("Enter m/s: "))
                        print(f"{ms:.2f} m/s = {ms*3.6:.2f} km/h")
                    elif conv == "2":
                        kmh = float(input("Enter km/h: "))
                        print(f"{kmh:.2f} km/h = {kmh/3.6:.2f} m/s")
                    elif conv == "3":
                        break
                    else:
                        print("Invalid option. Please select 1-3.")

            elif selection == "6":
                break

            else:
                print("Invalid option. Please select 1-6.")

    # ---------------- QUIT ----------------
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option. Please select 1-4.")