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

def run_improper_analysis():
    # p=2 (Convergent) vs p=1 (Divergent)
    x = np.linspace(1, 20, 500)
    y_conv = 1 / x**2
    y_div = 1 / x

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Convergent Plot
    ax1.plot(x, y_conv, 'g', lw=2, label='$1/x^2$ (Convergent)')
    ax1.fill_between(x, y_conv, color='green', alpha=0.2)
    ax1.set_title("Finite Area in Infinite Domain")
    ax1.legend()

    # Divergent Plot
    ax2.plot(x, y_div, 'r', lw=2, label='$1/x$ (Divergent)')
    ax2.fill_between(x, y_div, color='red', alpha=0.2)
    ax2.set_title("Infinite Area in Infinite Domain")
    ax2.legend()

    plt.suptitle("Lesson 17: Analysis of Improper Integrals", fontsize=16)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/17_improper_integral.png')
    plt.show()

if __name__ == "__main__":
    run_improper_analysis()
