from force_resultant_calculator_functions import validate_magnitude as validate
import math


def triangle_solver():
    side_a = validate("Enter length of side a: ")
    side_b = validate("Enter length of side b: ")
    angle_c = validate("Enter the included angle (in degrees): ")

    angle_c = math.radians(angle_c)

    side_c = math.sqrt(side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(angle_c))

    area = 0.5 * side_a * side_b * math.sin(angle_c)

    print("\nTriangle Results")
    print("-------------------")
    print(f"Third side (c): {side_c:.2f}")
    print(f"Area of triangle: {area:.2f}")