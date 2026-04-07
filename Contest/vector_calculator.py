from force_resultant_calculator_functions2 import validate_integer, validate_magnitude
import math 
import matplotlib.pyplot as plt
import numpy as np

def vector_collector():
    counter = validate_integer("Enter number of forces per Vector: ")
    vectors = {}
    for i in range(2):
        print(f"Vector{i+1}:")
        forces = []
        for j in range(counter):
            force = validate_magnitude(f"{j+1}: ")
            forces.append(force)
        vectors[f"Vector{i+1}"] = forces
    return vectors

def vector_collector_for_cross_product():
    vectors = {}
    for i in range(2):
        print(f"Vector{i+1}:")
        forces = []
        for j in range(3):
            force = validate_magnitude(f"{j+1}: ")
            forces.append(force)
        vectors[f"Vector{i+1}"] = forces
    return vectors

def dot_product():
    vectors = vector_collector()
    vector_list = list(vectors.values())
    v1 = vector_list[0]
    v2 = vector_list[1]

    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]

    print("\n--- Dot Product Result ---")
    print(f"Vector1 = {v1}")
    print(f"Vector2 = {v2}")
    print(f"Dot Product = {result}")
    
def cross_product():
    vectors = vector_collector_for_cross_product()
    v1 = vectors["Vector1"]
    v2 = vectors["Vector2"]
    
    cx = v1[1]*v2[2] - v1[2]*v2[1]
    cy = v1[2]*v2[0] - v1[0]*v2[2]
    cz = v1[0]*v2[1] - v1[1]*v2[0]
    
    cross = [cx,cy,cz]
    
    plot_vectors_3d(v1, v2, cross)
    print("\n--- Cross Product Result ---")
    print(f"Vector1 = {v1}")
    print(f"Vector2 = {v2}")
    print(f"Cross Product = [{cx:.0f}, {cy:.0f}, {cz:.0f}]")

def angle_between_vectors():
    vectors = vector_collector()
    v1 = vectors["Vector1"]
    v2 = vectors["Vector2"]
    
    # Calculate dot product
    dot = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
    
    # Calculate magnitudes
    mag1 = 0
    mag2 = 0
    for i in range(len(v1)):
        mag1 += v1[i]**2
        mag2 += v2[i]**2
    mag1 = math.sqrt(mag1)
    mag2 = math.sqrt(mag2)
    
    # Angle in degrees
    if mag1 == 0 or mag2 == 0:
        print("Cannot compute angle with a zero vector.")
        return
    
    angle_rad = math.acos(dot / (mag1 * mag2))
    angle_deg = math.degrees(angle_rad)
    
    print("\n--- Angle Between Vectors ---")
    print(f"Vector1 = {v1}")
    print(f"Vector2 = {v2}")
    print(f"Angle = {angle_deg:.2f}°")
    
    plot_angle(v1,v2,angle_deg)

def vector_magnitude():
    counter = validate_integer("Enter number of forces in the Vector: ")
    vector = []
    for j in range(counter):
        force = validate_magnitude(f"{j+1}: ")
        vector.append(force)
    
    mag = 0
    for component in vector:
        mag += component**2
    mag = math.sqrt(mag)
    
    print("\n--- Vector Magnitude ---")
    print(f"Vector = {vector}")
    print(f"Magnitude = {mag:.2f}")
        
            
        
def plot_vectors_3d(v1, v2, v3):
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')

    origin = np.array([0, 0, 0])
#%%
    # Vector 1
    ax.quiver(*origin, v1[0], v1[1], v1[2],
              linewidth=2,color = "blue", arrow_length_ratio=0.08)
    ax.text(v1[0], v1[1], v1[2], "Vector 1")

    # Vector 2
    ax.quiver(*origin, v2[0], v2[1], v2[2],
              linewidth=2, color = "red", arrow_length_ratio=0.08)
    ax.text(v2[0], v2[1], v2[2], "Vector 2")

    # Resultant (v3)
    ax.quiver(*origin, v3[0], v3[1], v3[2],
              linewidth=2, color = 'magenta' arrow_length_ratio=0.08)
    ax.text(v3[0], v3[1], v3[2], "Cross Product")
#%%
    # Origin
    ax.scatter(0, 0, 0)
    ax.text(0, 0, 0, 'O')

    max_range = 0
    for i in range(len(v1)):
        if(v1[i] > max_range):
            max_range = v1[i] 
        if(v2[i] > max_range):
            max_range = v2[i] 
        if(v3[i] > max_range):
            max_range = v3[i]
            
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    # Axis lines
    ax.plot([-max_range, max_range], [0, 0], [0, 0], linewidth=1, color = "black")
    ax.plot([0, 0], [-max_range, max_range], [0, 0], linewidth=1, color = "black")
    ax.plot([0, 0], [0, 0], [-max_range, max_range], linewidth=1, color = "black")

    # Labels
    ax.set_xlabel('X', labelpad=10)
    ax.set_ylabel('Y', labelpad=10)
    ax.set_zlabel('Z', labelpad=10)

    ax.set_title("Cross Product Diagram")

    ax.view_init(elev=25, azim=40)
    plt.show()
    
def plot_angle(v1,v2,angle):
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid()

    # Axes
    ax.plot([-10, 10], [0, 0], color="black")
    ax.plot([0, 0], [-10, 10], color="black")

    origin = np.array([0, 0])
  



    # Plot F1 and F2 from origin
    ax.quiver(*origin,v1[0],v1[1],
                  angles='xy', scale_units='xy', scale=1,
                  color="green",label = 'Vector 1')
    plt.text(v1[0], v1[1], "Vector 1")
    ax.quiver(*origin,v2[0],v2[1],
                  angles='xy', scale_units='xy', scale=1,
                  color="blue", label = 'Vector 2')
    plt.text(v2[0], v2[1], "Vector 2")
    
    #Angle between F1 and F2
    
    ax.text(1.8, 0.5, f"{angle:.1f}°", color='red')

    theta1 = np.arctan2(v1[1], v1[0])
    theta2 = np.arctan2(v2[1], v2[0])

    if theta2 < theta1:
        theta1, theta2 = theta2, theta1

    theta = np.linspace(theta1, theta2, 100)
    r = 2

    ax.plot(r*np.cos(theta), r*np.sin(theta), color='red')

    
    plt.legend
    plt.title("Angle between vectors")
    plt.show()


