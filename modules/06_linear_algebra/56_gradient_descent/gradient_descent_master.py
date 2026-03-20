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

def run_gd_master():
    # --- PROFESSIONAL PATH SETUP (Relative Path) ---
    asset_path = r'../../../assets'
    if not os.path.exists(asset_path):
        os.makedirs(asset_path)

    # 1. Cost Function Definition: J(w) = w^2 (Simple Convex Bowl)
    def cost_function(w):
        return w**2

    def gradient(w):
        return 2 * w

    # 2. Gradient Descent Simulation Parameters
    w = 4.0        # Initial starting point
    eta = 0.1      # Learning rate
    iterations = 30
    
    path_w = [w]
    path_cost = [cost_function(w)]

    # Optimization Loop
    for _ in range(iterations):
        w = w - eta * gradient(w)
        path_w.append(w)
        path_cost.append(cost_function(w))

    # --- 📸 ASSET 1: 2D CONVERGENCE PROGRESS (56_gd_2d.png) ---
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(path_cost)), path_cost, 'o-', color='#2980b9', lw=2, label='Cost J(w)')
    plt.title("2D Convergence: Cost Reduction via Gradient Descent", fontsize=14)
    plt.xlabel("Iteration Step")
    plt.ylabel("Cost Value")
    plt.grid(alpha=0.3)
    plt.legend()
    
    # Critical Fix: Save command for 2D
    save_path_2d = os.path.join(asset_path, '56_gd_2d.png')
    plt.savefig(save_path_2d, dpi=300)
    print(f"✅ 2D Asset saved: {save_path_2d}")
    plt.show()

    # --- 📸 ASSET 2: 3D OPTIMIZATION TRAJECTORY (56_gd_3d.png) ---
    fig = plt.figure(figsize=(12, 9))
    ax3d = fig.add_subplot(111, projection='3d')
    
    # Surface Data: J(w1, w2) = w1^2 + w2^2
    w1_vals = np.linspace(-5, 5, 100)
    w2_vals = np.linspace(-5, 5, 100)
    W1, W2 = np.meshgrid(w1_vals, w2_vals)
    Z = W1**2 + W2**2

    # Draw the objective surface
    surf = ax3d.plot_surface(W1, W2, Z, cmap='terrain', alpha=0.6, edgecolor='none')
    
    # Generate a synchronized 3D path for visualization
    # Starting from (4, -4) down to (0, 0)
    p_w1 = np.linspace(4, 0, 25)
    p_w2 = np.linspace(-4, 0, 25)
    p_z = p_w1**2 + p_w2**2
    
    ax3d.plot(p_w1, p_w2, p_z, 'r-o', markersize=5, lw=3, label='Descent Path')
    
    ax3d.set_title("3D Gradient Descent: Navigating the Cost Landscape", fontsize=14)
    ax3d.set_xlabel("Parameter W1")
    ax3d.set_ylabel("Parameter W2")
    ax3d.set_zlabel("Cost J(w)")
    ax3d.legend()
    
    # Optimal view angle for the 'bowl'
    ax3d.view_init(elev=35, azim=120)

    save_path_3d = os.path.join(asset_path, '56_gd_3d.png')
    plt.savefig(save_path_3d, dpi=300)
    print(f"✅ 3D Asset saved: {save_path_3d}")
    plt.show()

if __name__ == "__main__":
    run_gd_master()
