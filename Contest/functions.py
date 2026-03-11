from force_resultant_calculator_functions import *

def main():
    print("=====Welcome to Our Engineering Calculator!=====")
    menu = """
            1. Vector Calculator
            2. Quadratic Equation Solver
            3. Triangle Solver
            4. Force Resultant Calculator
            5. Unit Converter
            6.Quit
    """
    while True:
        print(menu)
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                options = """
                    1.Vector magnitude
                    2.Dot product
                    3.Angle between vectors
                    4.Cross product
                    5.back
                """
                while True:
                    print(options)
                    option = input("Enter your choice: ")
                    match option:
                        case "1":
                            vector_magnitude()
                        case "2":
                            dot_product()
                        case "3":
                            angle_between_vectors()
                        case "4":
                            cross_product()
                        case "5":
                            break
                        case _:
                            print("Invalid option. Please select 1-5.")

            case "2":
                quadratic_equation_solver()
            case "3":
                triangle_solver()
            case "4":
                alternatives = """
                        1. Force with two components(x,y)
                        2. Force with three components(x,y,z)
                        3. back
                """
                while True:
                    print(alternatives)
                    alternative = input("Enter your choice: ")
                    match alternative:
                        case "1":
                            vector_calculator_for_two_components()
                        case "2":
                            vector_calculator_for_three_components()
                        case "3":
                            break
                        case _:
                            print("Invalid option. Please select 1-3.")

            case "5":
                selections = """
                        1. meters -> feet
                        2. feet -> meters
                        3. kilograms -> pounds
                        4. pounds -> kilograms
                        5. seconds -> minutes
                        6. minutes -> seconds
                        7. celsius -> fahrenheit
                        8. fahrenheit -> celsius
                        9. meters/second -> kilometers/hour
                        10. kilometers/hour -> meters/second
                        11. back
                """
                while True:
                    print(selections)
                    selection = input("Enter your choice: ")
                    match selection:
                        case "1":
                            feet()
                        case "2":
                            meters()
                        case "3":
                            pounds()
                        case "4":
                            kilograms()
                        case "5":
                            minutes()
                        case "6":
                            seconds()
                        case "7":
                            fahrenheit()
                        case "8":
                            celsius()
                        case "9":
                            kilometers_per_hour()
                        case "10":
                            meters_per_second()
                        case "11":
                            break
                        case _:
                            print("Invalid option. Please select 1-11.")
            case "6":
                break
            case _:
                print("Invalid option. Please select 1-6.")


