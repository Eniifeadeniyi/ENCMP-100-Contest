from force_resultant_calculator_functions0 import validate_angle

import math
import matplotlib.pyplot as plt

def validate(prompt):
    while True:
        try:
            magnitude = float(input(prompt))
            if magnitude >0:
                return magnitude
            else:
               print("Please enter a positive number.") 
        except ValueError:
            print("Please enter a number.")
            
def SSS():
 a = validate("What is your first side ")
 b = validate("What is your second side ")
 c = validate("What is your third side ")
 while a+b <= c or a+c <= b or b+c <= a:
     print("Invalid triangle dimensions")
     a = validate("What is your first side ")
     b = validate("What is your second side ")
     c = validate("What is your third side ")
         
 A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
 B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
 C = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))
 drawTriangle(a,b,c,A,B,C)
 
def SSA1():
    a = validate("What is your first side ")
    b = validate("What is your second side ")
    C = validate_angle("What is your angle ")
    C_rad = math.radians(C)
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))
    A = math.degrees(math.asin(a*math.sin(C_rad)/c))
    B = 180 - A - C
    drawTriangle(a,b,c,A,B,C)
    
def SSA2():
    a = validate("What is your first side ")
    b = validate("What is your second side ")
    c = math.sqrt(a**2 + b**2)
    C = 90
    A = math.degrees(math.asin(a/c))
    B = 90 - A
    drawTriangle(a, b, c, A, B, C)
 
def drawTriangle(a, b, c, A, B, C):
    Ax, Ay = 0, 0
    Bx, By = c, 0

   # Coordinates
    Ax, Ay = 0, 0
    Bx, By = c, 0
    
    xC = (b**2 + c**2 - a**2) / (2 * c)
    yC = math.sqrt(max(0, b**2 - xC**2))

    # Create figure
    plt.figure(figsize=(6,6))
    
    # Draw triangle edges with color
    plt.plot([Ax, Bx], [Ay, By], linewidth=2)  # AB
    plt.plot([Bx, xC], [By, yC], linewidth=2)  # BC
    plt.plot([xC, Ax], [yC, Ay], linewidth=2)  # CA

    # Fill triangle lightly
    plt.fill([Ax, Bx, xC], [Ay, By, yC], alpha=0.1)

    # Plot vertices
    plt.scatter([Ax, Bx, xC], [Ay, By, yC], s=50)

    # Label vertices (slightly offset for clarity)
    plt.text(Ax, Ay-0.3, 'A', fontsize=12, ha='center')
    plt.text(Bx, By-0.3, 'B', fontsize=12, ha='center')
    plt.text(xC, yC+0.3, 'C', fontsize=12, ha='center')

    # Label sides
    midAB = ((Ax + Bx)/2, (Ay + By)/2)
    midBC = ((Bx + xC)/2, (By + yC)/2)
    midCA = ((xC + Ax)/2, (yC + Ay)/2)
    plt.text(*midAB, f'{c}', fontsize=10, ha='center', va='bottom')
    plt.text(*midBC, f'{a}', fontsize=10, ha='left')
    plt.text(*midCA, f'{b}', fontsize=10, ha='right')

    # Label angles at vertices
    plt.text(Ax-0.3, Ay+0.1, f'{A:.1f}°', fontsize=10, color='purple')
    plt.text(Bx+0.2, By+0.1, f'{B:.1f}°', fontsize=10, color='purple')
    plt.text(xC, yC+0.3, f'{C:.1f}°', fontsize=10, color='purple')
    
    # Clean up axes
    plt.title("Triangle", fontsize=14)
    plt.axis('equal')
    plt.axis('off')  # removes ugly axes

    plt.show()
    plt.close('all')

    


