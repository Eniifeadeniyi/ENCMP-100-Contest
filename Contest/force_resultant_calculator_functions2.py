import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter



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
    plot_vectors_2d(two_components, Rx, Ry)
    animate_2d_vectors(two_components)
    
    
   
    
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
    plot_vectors_3d(three_components, Rx, Ry, Rz)


def plot_vectors_2d(two_components, Rx, Ry):
    plt.figure()

    origin_x, origin_y = 0, 0

    # Plot each force
    for key, value in two_components.items():
        Fx = value["Fx"]
        Fy = value["Fy"]
        plt.quiver(origin_x, origin_y, Fx, Fy, angles='xy', scale_units='xy', scale=1)
        plt.text(Fx, Fy, key)

    # Plot resultant vector
    plt.quiver(origin_x, origin_y, Rx, Ry, angles='xy', scale_units='xy', scale=1)
    plt.text(Rx, Ry, "Resultant")

    # Axes settings
    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Force Vector Diagram")

    plt.show()
    plt.close('all')



def plot_vectors_3d(three_components, Rx, Ry, Rz):
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')

    origin = np.array([0, 0, 0])

    # Colors
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:red']

    # -------------------------------
    # 1. Draw vectors from origin
    # -------------------------------
    for i, (key, value) in enumerate(three_components.items()):
        vec = np.array([value["Fx"], value["Fy"], value["Fz"]])

        ax.quiver(*origin, *vec,
                  color=colors[i % len(colors)],
                  linewidth=2,
                  arrow_length_ratio=0.08,
                  alpha=0.6)

        ax.text(*(vec * 1.1), key, fontsize=10)

    # -------------------------------
    # 2. Tip-to-tail addition path
    # -------------------------------
    current_point = origin.copy()

    for i, (key, value) in enumerate(three_components.items()):
        vec = np.array([value["Fx"], value["Fy"], value["Fz"]])

        ax.quiver(*current_point, *vec,
                  color= 'black',
                  linewidth=3,
                  arrow_length_ratio=0.1)

        next_point = current_point + vec

        # Label along the segment
        mid_point = (current_point + next_point) / 2
        ax.text(*mid_point, key, fontsize=9)

        current_point = next_point

    final_point = current_point

    # -------------------------------
    # 3. Resultant vector
    # -------------------------------
    ax.quiver(0, 0, 0, Rx, Ry, Rz,
              color='black',
              linewidth=4,
              arrow_length_ratio=0.12)

    ax.text(Rx*1.1, Ry*1.1, Rz*1.1,
            "Resultant",
            fontsize=12,
            weight='bold')

    # -------------------------------
    # 4. Origin + axes
    # -------------------------------
    ax.scatter(0, 0, 0, color='black', s=50)
    ax.text(0, 0, 0, 'O', fontsize=12, weight='bold')

    # Axis limits
    all_vals = [Rx, Ry, Rz]
    for v in three_components.values():
        all_vals.extend([v["Fx"], v["Fy"], v["Fz"]])

    max_range = max(abs(val) for val in all_vals) * 1.2

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

    ax.set_title("3D Force Vector Addition (Engineering Diagram)", fontsize=14)

    # Clean look
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(True, linestyle='--', alpha=0.3)

    # Good viewing angle
    ax.view_init(elev=25, azim=40)

    plt.tight_layout()
    plt.show()
    plt.close('all')


def animate_2d_vectors(two_components, filename="force_resultant_2d.gif"):
    fig, ax = plt.subplots()

    # Dynamic axis scaling
    max_val = max(
        max(abs(v["Fx"]) for v in two_components.values()),
        max(abs(v["Fy"]) for v in two_components.values())
    ) * 2

    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Force Resultant Visualization")
    ax.grid(True)
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_aspect('equal', adjustable='box')

    # Color map for forces
    colors = plt.cm.tab10.colors

    arrows = []
    labels = []

    # Resultant path tracking
    path_x = [0]
    path_y = [0]
    path_line, = ax.plot([], [], 'k--', linewidth=1, label="Resultant Path")

    metadata = dict(title="Force Resultant", artist="ForceCalc")
    writer = PillowWriter(fps=15, metadata=metadata)

    forces_list = list(two_components.items())
    Rx_cumulative, Ry_cumulative = 0, 0
    steps_per_force = 20

    with writer.saving(fig, filename, 100):

        # Initial resultant
        res_arrow = ax.arrow(0, 0, 0, 0, head_width=0.4, color='red')
        res_text = ax.text(0, 0, "R", color='red')
        
        # Keep track of all previous arrows so they don't disappear
        permanent_arrows = []
        permanent_labels = []


        for i, (key, value) in enumerate(forces_list):
            Fx_full, Fy_full = value["Fx"], value["Fy"]
            
            start_point = np.array([Rx_cumulative, Ry_cumulative])
            color = colors[i % len(colors)]

            for t in np.linspace(0, 1, steps_per_force):
                Fx = Fx_full * t
                Fy = Fy_full * t

                # Remove last force arrow
                if arrows:
                    arrows[-1].remove()
                    labels[-1].remove()

                # Draw force
                arrow = ax.arrow(0, 0, Fx, Fy, head_width=0.3, color=color)
                label = ax.text(Fx, Fy, key, color=color)

                arrows.append(arrow)
                labels.append(label)

                # Update resultant
                Rx_current = Rx_cumulative + Fx
                Ry_current = Ry_cumulative + Fy

                res_arrow.remove()
                res_text.remove()

                res_arrow = ax.arrow(0, 0, Rx_current, Ry_current,
                                     head_width=0.5, color='red')
                res_text = ax.text(Rx_current, Ry_current, "R", color='red')

                writer.grab_frame()
            # After finishing the animation of this vector, make it permanent
            perm_arrow = ax.arrow(0, 0, Fx_full, Fy_full, head_width=0.3, color=color)
            perm_label = ax.text(0+Fx_full, start_point[1]+Fy_full, key)
            permanent_arrows.append(perm_arrow)
            permanent_labels.append(perm_label)


            # Update cumulative
            Rx_cumulative += Fx_full
            Ry_cumulative += Fy_full

            # Update path (tip-to-tail)
            path_x.append(Rx_cumulative)
            path_y.append(Ry_cumulative)
            path_line.set_data(path_x, path_y)

        # Final frame with full path
        writer.grab_frame()

    # Add legend AFTER animation setup
    handles = []
    for i, key in enumerate(two_components.keys()):
        handles.append(plt.Line2D([0], [0], color=colors[i % len(colors)], lw=2, label=key))

    handles.append(plt.Line2D([0], [0], color='red', lw=2, label="Resultant"))
    handles.append(plt.Line2D([0], [0], color='black', linestyle='--', lw=2, label="Path"))

    ax.legend(handles=handles, loc='upper right')
    plt.close('all')
    print(f"Animation saved as {filename}")
    

