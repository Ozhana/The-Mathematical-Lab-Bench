# -*- coding: utf-8 -*-
"""
The Mathematical Lab Bench
---------------------------
Project Author: Dr. Ozhan Akdag
Academic Role: PhD in Mathematics & PhD in Education
License: MIT License
Created: 2026

Description: Part of a comprehensive mathematical computational laboratory.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def run_polar_analysis():
    theta = np.linspace(0, 2*np.pi, 500)
    # Cardioid: r = 1 + cos(theta)
    r = 1 + np.cos(theta)
    
    # Polar to Cartesian conversion for plotting
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    fig = plt.figure(figsize=(12, 6))
    
    # 1. Standart Polar Plot
    ax1 = fig.add_subplot(121, projection='polar')
    ax1.plot(theta, r, color='magenta', lw=2)
    ax1.fill(theta, r, color='magenta', alpha=0.2)
    ax1.set_title("Polar Representation", va='bottom')

    # 2. Cartesian Space Representation (Daha 'Matematiksel' Bakış)
    ax2 = fig.add_subplot(122)
    ax2.plot(x, y, color='magenta', lw=2)
    ax2.fill(x, y, color='magenta', alpha=0.1)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.set_title("Cartesian Mapping ($x=r\cosθ, y=r\sinθ$)")

    plt.suptitle("Lesson 19: Area Analysis in Polar Systems", fontsize=16)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/19_polar_area.png')
    plt.show()

if __name__ == "__main__":
    run_polar_analysis()
