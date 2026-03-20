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

def run_newton_raphson():
    # Function f(x) = x^2 - 2 (Looking for sqrt(2))
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    
    x_range = np.linspace(0.5, 2.5, 100)
    x_n = 2.0  # Initial guess
    iterations = 3
    
    plt.figure(figsize=(10, 7))
    plt.plot(x_range, f(x_range), 'k', lw=2, label='$f(x) = x^2 - 2$')
    plt.axhline(0, color='black', lw=1)
    
    colors = ['red', 'green', 'orange']
    
    for i in range(iterations):
        y_n = f(x_n)
        slope = df(x_n)
        
        # Plot tangent line: y = slope*(x - x_n) + y_n
        # X-intercept of tangent is x_next = x_n - y_n/slope
        x_next = x_n - y_n/slope
        
        t_range = np.linspace(x_next - 0.2, x_n + 0.2, 10)
        plt.plot(t_range, slope*(t_range - x_n) + y_n, '--', color=colors[i], 
                 label=f'Iteration {i+1}: $x_{i+1}$={x_next:.4f}')
        plt.scatter([x_n], [y_n], color=colors[i], zorder=5)
        
        x_n = x_next

    plt.title("Lesson 10: Newton-Raphson Convergence Steps", fontsize=14)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/10_newton_raphson.png')
    plt.show()

if __name__ == "__main__":
    run_newton_raphson()
