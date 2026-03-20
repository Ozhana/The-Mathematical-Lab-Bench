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

def run_area_between():
    x = np.linspace(0, 1.2, 100)
    f = np.sqrt(x)
    g = x**2

    plt.figure(figsize=(10, 6))
    plt.plot(x, f, 'b', lw=2, label='$f(x) = \sqrt{x}$')
    plt.plot(x, g, 'r', lw=2, label='$g(x) = x^2$')
    
    # Kesişim bölgesini doldur (0 ile 1 arası)
    x_fill = np.linspace(0, 1, 50)
    plt.fill_between(x_fill, np.sqrt(x_fill), x_fill**2, color='purple', alpha=0.2, label='Enclosed Area')

    plt.title("Lesson 14: Area Between Two Curves", fontsize=14)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/14_area_between_curves.png')
    plt.show()

if __name__ == "__main__":
    run_area_between()
