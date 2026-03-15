from force_resultant_calculator_functions import validate_magnitude as validate
import math

def quadratic_equation_solver():
    x_square_coeff = validate("Enter coefficient of x²: ")
    x_coeff = validate("Enter coefficient of x: ")
    constant = validate("Enter value of the constant: ")

    discriminant = x_coeff ** 2 - 4 * x_square_coeff * constant

    if discriminant > 0:
        x1 = (-x_coeff + math.sqrt(discriminant)) / (2 * x_square_coeff)
        x2 = (-x_coeff - math.sqrt(discriminant)) / (2 * x_square_coeff)

        print(f"The values of x are {x1:.2f} and {x2:.2f}")

    elif discriminant == 0:
        x = -x_coeff / (2 * x_square_coeff)

        print(f"The equation has one real solution: x = {x:.2f}")

    else:
        print("The equation has no real solutions.")