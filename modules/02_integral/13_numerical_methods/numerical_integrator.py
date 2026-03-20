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

def f(x): return 1 / (1 + x**2)

def run_numerical_comparison():
    a, b = 0, 3
    n = 6 # Düşük n değeri farkı daha iyi gösterir
    x = np.linspace(a, b, 100)
    x_n = np.linspace(a, b, n + 1)
    y_n = f(x_n)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # 1. Trapezoidal Visualization
    ax1.plot(x, f(x), 'k', lw=2)
    ax1.fill_between(x_n, y_n, alpha=0.3, color='orange', edgecolor='black', step=None)
    for i in range(n + 1):
        ax1.vlines(x_n[i], 0, y_n[i], color='gray', linestyle='--', alpha=0.5)
    ax1.set_title(f"Trapezoidal Rule (n={n})", fontsize=12)

    # 2. Simpson's Rule Logic (Parabolic approximation)
    ax2.plot(x, f(x), 'k', lw=2)
    ax2.fill_between(x, f(x), alpha=0.1, color='blue') # Gerçek alan
    # Simpson noktalarını vurgula
    ax2.scatter(x_n, y_n, color='red', zorder=5)
    ax2.set_title(f"Simpson's Rule (Quadratic Fit)", fontsize=12)

    plt.suptitle("Lesson 13: Comparing Numerical Integration Methods", fontsize=14)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/13_numerical_methods.png')
    plt.show()

if __name__ == "__main__":
    run_numerical_comparison()
