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

# f(x) = (x^2 - 1) / (x - 1) -> x=1'de delik var ama limit 2
x = np.linspace(0.5, 1.5, 100)
y = (x**2 - 1) / (x - 1)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = (x²-1)/(x-1)', color='blue')
plt.scatter([1], [2], color='red', s=100, facecolors='none', label='Hole at L=2')

# Epsilon-Delta visualization
plt.axhspan(1.9, 2.1, alpha=0.1, color='green', label='Epsilon (y-range)')
plt.axvspan(0.95, 1.05, alpha=0.1, color='orange', label='Delta (x-range)')

plt.title("Lesson 01: Epsilon-Delta Definition of Limits", fontsize=14)
plt.legend()
plt.savefig('assets/01_limit_epsilon.png')
plt.show()
