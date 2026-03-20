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
import seaborn as sns
import os

def run_gaussian_viz():
    # 3x3 bir sistem: Ax = b (Float olarak tanımlıyoruz ki bölme hatası olmasın)
    A = np.array([[2.0, 1.0, -1.0],
                  [-3.0, -1.0, 2.0],
                  [-2.0,  1.0, 2.0]])
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Adım 0: Orijinal Matris
    sns.heatmap(A, annot=True, cmap='YlGnBu', ax=axes[0], cbar=False, fmt=".2f", linewidths=1)
    axes[0].set_title("1. Original Matrix", fontsize=12, fontweight='bold')

    # Adım 1: İlk sütun temizliği (Pivot: A[0,0])
    # Alt satırlardaki ilk sütun elemanlarını sıfırlıyoruz
    A[1] = A[1] - (A[1,0] / A[0,0]) * A[0]
    A[2] = A[2] - (A[2,0] / A[0,0]) * A[0]
    
    sns.heatmap(A, annot=True, cmap='YlGnBu', ax=axes[1], cbar=False, fmt=".2f", linewidths=1)
    axes[1].set_title("2. First Column Eliminated", fontsize=12, fontweight='bold')

    # Adım 2: İkinci sütun temizliği (Pivot: A[1,1])
    # Son satırdaki ikinci sütun elemanını sıfırlıyoruz
    A[2] = A[2] - (A[2,1] / A[1,1]) * A[1]
    
    sns.heatmap(A, annot=True, cmap='YlGnBu', ax=axes[2], cbar=False, fmt=".2f", linewidths=1)
    axes[2].set_title("3. Upper Triangular Form", fontsize=12, fontweight='bold')

    plt.suptitle("Lesson 24: Gaussian Elimination Process (Row Echelon Form)", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    if not os.path.exists('../../../assets'): 
        os.makedirs('../../../assets')
    plt.savefig('../../../assets/24_gaussian_elimination.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_gaussian_viz()
