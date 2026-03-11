import math
def validate_magnitude(prompt):
    while True:
        try:
            magnitude = float(input(prompt))
            return magnitude
        except ValueError:
            print("Please enter a number.")

def validate_angle(prompt):
    while True:
        try:
            angle = float(input(prompt))
            if 0 <= angle <= 360:
                return math.radians(angle)
            else:
                print("Angle must be between 0 and 360 degrees.")
        except ValueError:
            print("Please enter a number.")

def validate_integer(prompt):
    while True:
        try:
            integer = int(input(prompt))
            return integer
        except ValueError:
            print("Please enter a whole number.")

def force_collector_of_two_components():
    count = validate_integer("Enter number of forces: ")
    two_components = {}
    for i in range(count):
        magnitude = validate_magnitude(f"Enter magnitude(N) of Force{i+1}: ")
        angle = validate_angle(f"Enter angle(degrees) of Force{i+1}: ")
        x_component = round(magnitude * math.cos(angle), 2)
        y_component = round(magnitude * math.sin(angle), 2)
        two_components[f"Force{i+1}"] = {"Fx" : x_component, "Fy" : y_component}
    return two_components

def force_collector_of_three_components():
    count = validate_integer("Enter number of forces: ")
    three_components = {}
    for i in range(count):
        print(f"Force{i+1}:")
        x_component = validate_magnitude("Fx: ")
        y_component = validate_magnitude("Fy: ")
        z_component = validate_magnitude("Fz: ")
        three_components[f"Force{i+1}"] = {"Fx" : x_component, "Fy" : y_component, "Fz" : z_component}
    return three_components

def vector_calculator_for_two_components():
    two_components = force_collector_of_two_components()
    x_components = (force["Fx"] for force in two_components.values())
    y_components = (force["Fy"] for force in two_components.values())
    
    Rx = sum(x_components)
    Ry = sum(y_components)
    
    R = math.sqrt(Rx ** 2 + Ry **2)
    direction = math.degrees(math.atan2(Ry,Rx))
    
    print("--- Force Components ---")
    print(f"{'Force':<10}{'Fx(N)':>10}{'Fy(N)':>10}")
    
    for key,value in two_components.items():
        print(f"{key:<10}{value['Fx']:>10.2f}{value['Fy']:>10.2f}")
        
    print("Resultant Force: ")
    print(f"{'Rx(N)':<15}: {Rx:.2f}")
    print(f"{'Ry(N)':<15}: {Ry:.2f}")
    print(f"{'Magnitude(N)':<15}: {R:.2f}")
    print(f"{'Direction(°)':<15}: {direction:.2f}")
    
def vector_calculator_for_three_components():
    three_components = force_collector_of_three_components()
    
    x_components = (force["Fx"] for force in three_components.values())
    y_components = (force["Fy"] for force in three_components.values())
    z_components = (force["Fz"] for force in three_components.values())
    
    Rx = sum(x_components)
    Ry = sum(y_components)
    Rz = sum(z_components)
    
    R = math.sqrt(Rx ** 2 + Ry ** 2 + Rz ** 2)
    
    print("--- Force Components (3D) ---")
    print(f"{'Force':<10}{'Fx(N)':>10}{'Fy(N)':>10}{'Fz(N)':>10}")

    for key, value in three_components.items():
        print(f"{key:<10}{value['Fx']:>10.2f}{value['Fy']:>10.2f}{value['Fz']:>10.2f}")
    
    print("\n--- Resultant Force ---")
    print(f"{'Rx(N)':<15}: {Rx:.2f}")
    print(f"{'Ry(N)':<15}: {Ry:.2f}")
    print(f"{'Rz(N)':<15}: {Rz:.2f}")
    print(f"{'Magnitude(N)':<15}: {R:.2f}")
    
    