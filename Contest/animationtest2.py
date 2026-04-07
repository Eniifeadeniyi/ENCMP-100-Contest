# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:21:38 2026

@author: aimee
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

def animate_2d_vectors(two_components, filename="force_resultant_2d.gif"):
    fig, ax = plt.subplots()
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Smooth Force Resultant Animation")
    ax.grid(True)
    ax.axhline(0)
    ax.axvline(0)
    ax.set_aspect('equal', adjustable='box') 
    
    arrows = []
    arrow_labels = []
    
    metadata = dict(title="Force Resultant 2D", artist="ForceCalc")
    writer = PillowWriter(fps=15, metadata=metadata)
    
    forces_list = list(two_components.items())
    Rx_cumulative, Ry_cumulative = 0, 0
    steps_per_force = 20
    
    with writer.saving(fig, filename, 100):
        # Initialize resultant arrow
        res_arrow = ax.arrow(0, 0, 0, 0, head_width=0.5, color='red')
        res_text = ax.text(0, 0, "Resultant")
        
        for key, value in forces_list:
            Fx_full, Fy_full = value["Fx"], value["Fy"]
            
            for t in np.linspace(0, 1, steps_per_force):
                Fx = Fx_full * t
                Fy = Fy_full * t
                
                # Remove previous force arrow and label
                if arrows:
                    arrows[-1].remove()
                    arrow_labels[-1].remove()
                
                # Draw current force
                arrow = ax.arrow(0, 0, Fx, Fy, head_width=0.3, color='blue')
                label = ax.text(Fx, Fy, key)
                arrows.append(arrow)
                arrow_labels.append(label)
                
                # Update cumulative resultant
                Rx_current = Rx_cumulative + Fx
                Ry_current = Ry_cumulative + Fy
                
                res_arrow.remove()
                res_text.remove()
                
                res_arrow = ax.arrow(0, 0, Rx_current, Ry_current, head_width=0.5, color='red')
                res_text = ax.text(Rx_current, Ry_current, "Resultant")
                
                writer.grab_frame()
            
            # Update cumulative total after this force finishes
            Rx_cumulative += Fx_full
            Ry_cumulative += Fy_full
            
            
            
if __name__ == "__main__":
    test_case = {
        "F1": {"Fx": 5, "Fy": 2,},
        "F2": {"Fx": -3, "Fy": 4},
        "F3": {"Fx": 2, "Fy": -5}
    }

animate_2d_vectors(test_case)