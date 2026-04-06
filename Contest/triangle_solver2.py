import math
import matplotlib.pyplot as plt
def main():
 print()
 print("Please input givens for the equation")  
 print("0. 3 sides ")
 print("1. 2 sides one angle")
 print("1. 2 sides - right triangle")
 choice = int(input("What is your choice?"))

 if choice == 0:
  a = int(input("What is your first side "))
  b = int(input("What is your second side "))
  c = int(input("What is your third side "))
  
  SSS(a,b,c)
 elif choice == 1 :
  a = int(input("What is your first side "))
  b = int(input("What is your second side "))
  C = int(input("What is your angle "))
  
  SSA1(a,b,C)
 elif choice == 2:
  a = int(input("What is your first side "))
  b = int(input("What is your second side "))
  SSA2(a,b)
 
    
def SSS (a,b,c):
 A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
 B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
 C = math.degrees(math.acos((b**2+a**2-c**2)/(2*b*a)))
 
 drawTriangle(a,b,c,A,B,C)
 
def SSA1(a,b,C):
    C_rad = math.radians(C)
    
    c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))
    
    A = math.degrees(math.asin(a*math.sin(C_rad)/c))
    B = 180 - A - C
    
    drawTriangle(a,b,c,A,B,C)
    
def SSA2(a,b):
    c = math.sqrt(a**2 + b**2)
    
    C = 90
    A = math.degrees(math.asin(a/c))
    B = 90 - A
 
def drawTriangle(a, b, c, A, B, C):
    Ax, Ay = 0, 0
    Bx, By = c, 0

    # Coordinates of point C
    xC = (b**2 + c**2 - a**2) / (2*c)
    yC = math.sqrt(abs(b**2 - xC**2))

    # Plot triangle
    x = [Ax, Bx, xC, Ax]
    y = [Ay, By, yC, Ay]

    plt.figure()
    plt.plot(x, y, marker='o', linewidth=2)

    # ---- Label vertices ----
    plt.text(Ax, Ay, ' A', fontsize=12)
    plt.text(Bx, By, ' B', fontsize=12)
    plt.text(xC, yC, ' C', fontsize=12)

    # ---- Midpoints for side labels ----
    mid_AB = ((Ax + Bx)/2, (Ay + By)/2)
    mid_BC = ((Bx + xC)/2, (By + yC)/2)
    mid_CA = ((xC + Ax)/2, (yC + Ay)/2)

    # ---- Side labels ----
    plt.text(mid_AB[0], mid_AB[1] - 0.3, f'c = {c:.2f}', color='blue')
    plt.text(mid_BC[0] + 0.2, mid_BC[1], f'a = {a:.2f}', color='blue')
    plt.text(mid_CA[0] - 1, mid_CA[1], f'b = {b:.2f}', color='blue')

    # ---- Angle labels ----
    plt.text(Ax + 0.3, Ay + 0.1, f'A = {A:.1f}°', color='red')
    plt.text(Bx - 1.0, By + 0.1, f'B = {B:.1f}°', color='red')
    plt.text(xC - 0.4, yC -0.45, f'C = {C:.1f}°', color='red')

    # ---- Styling ----
    plt.title("Triangle Solution (Engineering Diagram)")
    plt.axis('equal')
    plt.grid(True)

    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()
    


def triangle_solver2():
    main()