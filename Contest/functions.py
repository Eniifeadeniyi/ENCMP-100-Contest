from force_resultant_calculator_functions import vector_calculator_for_two_components,vector_calculator_for_three_components
from unit_converter_functions import *
from quadratic_equation_solver_function import *
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
                        1. Length: meters <-> feet
                        2. Mass: kilograms <-> pounds
                        3. Time: seconds <-> minutes
                        4. Temperature: Celsius <-> Fahrenheit
                        5. Speed: m/s <-> km/h
                        6. back
                """
                while True:
                    print(selections)
                    selection = input("Enter your choice: ")
                    match selection:
                        case "1": #Length
                            length_menu = """
                            1. meters -> feet
                            2. feet -> meters
                            3. back
                            """
                            while True:
                                print(length_menu)
                                conversion = input("Enter your choice: ")
                                match conversion:
                                    case "1":
                                        feet()
                                    case "2":
                                        meters()
                                    case "3":
                                        break
                                    case _:
                                        print("Invalid option. Please select 1-3.")
                                        
                        case "2": #Mass
                            mass_menu = """
                            1. kilograms -> pounds
                            2. pounds -> kilograms
                            3. back
                            """
                            while True:
                                print(mass_menu)
                                conversion = input("Enter a choice: ")
                                match conversion:
                                    case "1":
                                        pounds()
                                    case "2":
                                        kilograms()
                                    case "3":
                                        break 
                                    case _: 
                                        print("Invalid option. Please select 1-3.")
                     
                        case "3": #Time
                            time_menu = """
                            1. seconds -> minutes
                            2. minutes -> seconds
                            3. Back
                            """
                            while True:
                                print(time_menu)
                                choice_time = input("Enter your choice: ")
                                match choice_time:
                                    case "1":
                                        minutes()
                                    case "2":
                                        seconds()
                                    case "3":
                                        break
                                    case _:
                                        print("Invalid option. Please select 1-3.")
                                                   
                        case "4":  # Temperature
                            temp_menu = """
                                1. Celsius -> Fahrenheit
                                2. Fahrenheit -> Celsius
                                3. Back
                            """
                            while True:
                                print(temp_menu)
                                choice_temp = input("Enter your choice: ")
                                match choice_temp:
                                    case "1":
                                        fahrenheit()
                                    case "2":
                                        celsius()
                                    case "3":
                                        break
                                    case _:
                                        print("Invalid option. Please select 1-3.")
            
                        case "5":  # Speed
                            speed_menu = """
                                1. meters/second -> kilometers/hour
                                2. kilometers/hour -> meters/second
                                3. Back
                            """
                            while True:
                                print(speed_menu)
                                choice_speed = input("Enter your choice: ")
                                match choice_speed:
                                    case "1":
                                        kilometers_per_hour()
                                    case "2":
                                        meters_per_second()
                                    case "3":
                                        break
                                    case _:
                                        print("Invalid option. Please select 1-3.")
                                    case "6":
                                        break
                                    case _:
                                        print("Invalid option. Please select 1-6.")
            case "6":
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid option. Please select 1-6.")


