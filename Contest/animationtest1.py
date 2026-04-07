# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 17:33:43 2026

@author: aimee
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

def animate_2d_vectors(vectors):
    fig, ax = plt.subplots()

    colors = ['r', 'g', 'b', 'c', 'm', 'y']

    # Dynamic scaling
    max_val = max(
        max(abs(v["Fx"]) for v in vectors.values()),
        max(abs(v["Fy"]) for v in vectors.values())
    ) * 2

    ax.set_xlim(-max_val, max_val)
    ax.set_ylim(-max_val, max_val)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)

    metadata = dict(title="2D Resultant", artist="Aimee")
    writer = PillowWriter(fps=2, metadata=metadata)

    origin = np.array([0, 0])
    current = origin.copy()

    text_objects = []  # track labels

    with writer.saving(fig, "2D_resultant.gif", 100):

        for i, (name, comp) in enumerate(vectors.items()):
            color = colors[i % len(colors)]

            Fx, Fy = comp["Fx"], comp["Fy"]

            # Draw vector
            ax.quiver(current[0], current[1],
                      Fx, Fy,
                      angles='xy', scale_units='xy', scale=1,
                      color=color)

            tip = current + np.array([Fx, Fy])

            # Offset text slightly so it's visible
            txt = ax.text(tip[0] + 0.2, tip[1] + 0.2, name, color=color)
            text_objects.append(txt)

            current = tip

            writer.grab_frame()

        # Final resultant
        ax.quiver(0, 0,
                  current[0], current[1],
                  angles='xy', scale_units='xy', scale=1,
                  color='k', linewidth=3)

        ax.text(current[0] + 0.2, current[1] + 0.2,
                "Resultant", color='k')

        writer.grab_frame()

    plt.close()
    
    
if __name__ == "__main__":
    test_case = {
        "F1": {"Fx": 5, "Fy": 2,},
        "F2": {"Fx": -3, "Fy": 4},
        "F3": {"Fx": 2, "Fy": -5}
    }

animate_2d_vectors(test_case)