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

def run_chain_rule():
    x = np.linspace(0, 3, 400)
    # Composite function: f(g(x)) = sin(x^2)
    y = np.sin(x**2)
    # Derivative via Chain Rule: f'(g(x))*g'(x) = cos(x^2) * 2x
    dy = 2*x * np.cos(x**2)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    ax1.plot(x, y, color='#2ecc71', lw=2, label='$f(x) = \sin(x^2)$')
    ax1.set_title("Composite Function", fontsize=12)
    ax1.legend()
    ax1.grid(alpha=0.3)

    ax2.plot(x, dy, color='#e67e22', lw=2, label="$f'(x) = 2x \cos(x^2)$")
    ax2.set_title("Derivative (Chain Rule Result)", fontsize=12)
    ax2.legend()
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    
    if not os.path.exists('../../../assets'):
        os.makedirs('../../../assets')
    plt.savefig('../../../assets/04_chain_rule.png')
    plt.show()

if __name__ == "__main__":
    run_chain_rule()
