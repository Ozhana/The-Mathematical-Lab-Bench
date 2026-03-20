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
from mpl_toolkits.mplot3d import Axes3D
import os

def generate_optimization_assets():
    # Fonksiyon: f(x,y) = x^2 - y^2 (Saddle Point)
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 - Y**2

    # Assets klasörü kontrolü
    asset_path = '../../../assets'
    if not os.path.exists(asset_path): os.makedirs(asset_path)

    # --- FIGURE 1: 3D Visualization ---
    fig3d = plt.figure(figsize=(10, 8))
    ax3d = fig3d.add_subplot(111, projection='3d')
    surf = ax3d.plot_surface(X, Y, Z, cmap='PiYG', alpha=0.8, edgecolor='none')
    ax3d.scatter([0], [0], [0], color='red', s=200, label='Saddle Point (0,0)')
    ax3d.set_title("3D Hyperbolic Paraboloid (Saddle)", fontsize=14)
    plt.savefig(f'{asset_path}/29_saddle_3d.png', dpi=300)
    
    # --- FIGURE 2: 2D Contour Visualization ---
    fig2d = plt.figure(figsize=(10, 8))
    ax2d = fig2d.add_subplot(111)
    cp = ax2d.contourf(X, Y, Z, 20, cmap='PiYG')
    plt.colorbar(cp)
    ax2d.axhline(0, color='black', lw=1, ls='--')
    ax2d.axvline(0, color='black', lw=1, ls='--')
    ax2d.plot(0, 0, 'ro', markersize=12, label='Critical Point')
    ax2d.set_title("2D Contour Map: Hyperbolic Signatures", fontsize=14)
    plt.savefig(f'{asset_path}/29_saddle_2d.png', dpi=300)

    # --- MASTER DASHBOARD: Show them together ---
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(20, 9))
    
    # Left: 3D Preview
    ax_left = fig.add_subplot(121, projection='3d')
    ax_left.plot_surface(X, Y, Z, cmap='PiYG', alpha=0.7)
    ax_left.set_title("3D View")
    
    # Right: 2D Preview
    ax_right.contourf(X, Y, Z, 20, cmap='PiYG')
    ax_right.set_title("2D Contour View")
    
    plt.suptitle("Lesson 29: Optimization & Saddle Point Analysis", fontsize=20)
    plt.show()

if __name__ == "__main__":
    generate_optimization_assets()
