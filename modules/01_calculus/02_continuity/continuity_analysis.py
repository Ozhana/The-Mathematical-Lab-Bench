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

def run_continuity_analysis():
    # Parçalı fonksiyon tanımı (Piecewise)
    x1 = np.linspace(-2, 0.95, 100)
    y1 = x1**2
    x2 = np.linspace(1.05, 3, 100)
    y2 = x2 + 2 

    plt.figure(figsize=(10, 6))
    plt.plot(x1, y1, 'b', lw=2.5, label='Left Limit Segment')
    plt.plot(x2, y2, 'r', lw=2.5, label='Right Limit Segment')
    
    # Boş ve dolu noktalar (Süreksizliği göstermek için)
    plt.scatter([1], [1], edgecolors='b', facecolors='none', s=100, zorder=5)
    plt.scatter([1], [3], color='r', s=100, zorder=5)

    plt.title("Lesson 02: Visualizing Jump Discontinuity", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    if not os.path.exists('../../../assets'):
        os.makedirs('../../../assets')
    plt.savefig('../../../assets/02_continuity.png')
    plt.show()

if __name__ == "__main__":
    run_continuity_analysis()
