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

def run_implicit():
    x = np.linspace(-6, 6, 400)
    y = np.linspace(-6, 6, 400)
    X, Y = np.meshgrid(x, y)
    
    # Equation: x^2 + y^2 = 25
    Z = X**2 + Y**2 - 25
    
    plt.figure(figsize=(8, 8))
    plt.contour(X, Y, Z, levels=[0], colors='blue', linewidths=2)
    
    # Tangent at (3, 4)
    px, py = 3, 4
    slope = -px / py
    tx = np.linspace(1, 5, 10)
    ty = slope * (tx - px) + py
    
    plt.plot(tx, ty, 'r--', lw=2, label=f'Tangent at (3,4) | m = {slope}')
    plt.scatter([px], [py], color='red', s=100)
    
    plt.title("Lesson 07: Implicit Differentiation (Circle)", fontsize=14)
    plt.gca().set_aspect('equal')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/07_implicit.png')
    plt.show()

if __name__ == "__main__":
    run_implicit()
