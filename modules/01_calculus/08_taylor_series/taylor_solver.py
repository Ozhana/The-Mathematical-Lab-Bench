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

def run_taylor():
    x = np.linspace(-2*np.pi, 2*np.pi, 200)
    y_actual = np.sin(x)
    
    # Taylor terms centered at a=0
    p1 = x
    p3 = x - (x**3)/6
    p5 = x - (x**3)/6 + (x**5)/120
    p7 = x - (x**3)/6 + (x**5)/120 - (x**7)/5040

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_actual, 'k', lw=3, label='Actual $\sin(x)$')
    plt.plot(x, p1, '--', label='1st Order (Linear)')
    plt.plot(x, p3, '--', label='3rd Order')
    plt.plot(x, p5, '--', label='5th Order')
    plt.plot(x, p7, '--', label='7th Order')

    plt.ylim(-2.5, 2.5)
    plt.title("Lesson 08: Taylor Series Convergence", fontsize=14)
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/08_taylor_series.png')
    plt.show()

if __name__ == "__main__":
    run_taylor()
