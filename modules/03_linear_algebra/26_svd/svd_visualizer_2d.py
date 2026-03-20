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

def run_svd_2d():
    # Rastgele bir 2x2 matris
    A = np.array([[2, 1], [1, 3]])
    U, S, Vt = np.linalg.svd(A)
    
    t = np.linspace(0, 2*np.pi, 100)
    circle = np.array([np.cos(t), np.sin(t)])

    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    # Adımları görselleştir
    titles = ['1. Original Circle', '2. After $V^T$ (Rotation)', '3. After $\Sigma$ (Scaling)', '4. After $U$ (Rotation)']
    current_points = circle
    
    # S matrisini diyagonal yap
    Sigma = np.diag(S)
    
    transforms = [np.eye(2), Vt, Sigma @ Vt, U @ Sigma @ Vt]

    for i, ax in enumerate(axes):
        pts = transforms[i] @ circle
        ax.plot(pts[0], pts[1], 'b-', lw=2)
        ax.fill(pts[0], pts[1], alpha=0.1, color='blue')
        ax.set_title(titles[i], fontweight='bold')
        ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
        ax.grid(True, alpha=0.3)
        ax.set_aspect('equal')

    plt.suptitle("Lesson 26: SVD as a Sequence of Geometric Operations", fontsize=16)
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/26_svd_2d.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_svd_2d()
