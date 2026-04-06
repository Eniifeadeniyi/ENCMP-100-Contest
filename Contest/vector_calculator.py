from force_resultant_calculator_functions2 import validate_integer, validate_magnitude

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
    pass

def angle_between_vectors():
    pass

def vector_magnitude():
    pass
    
        
    
    