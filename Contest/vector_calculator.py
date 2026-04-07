from force_resultant_calculator_functions2 import validate_integer, validate_magnitude
import math 

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

def vector_magnitude():
    vectors = vector_collector()
    v1 = vectors["Vector1"]
    
    mag = 0
    for component in v1:
        mag += component**2
    mag = math.sqrt(mag)
    
    print("\n--- Vector Magnitude ---")
    print(f"Vector = {v1}")
    print(f"Magnitude = {mag:.2f}")
        
            
        
        