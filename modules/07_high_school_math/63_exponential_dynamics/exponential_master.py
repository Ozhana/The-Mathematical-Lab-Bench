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

def run_exponential_master():
    asset_path = r'../../../assets'
    if not os.path.exists(asset_path): os.makedirs(asset_path)

    # 1. 2D Data: Linear vs Exponential
    t = np.linspace(0, 10, 100)
    linear = 20 * t + 50
    exponential = 50 * np.exp(0.4 * t)

    # --- 📸 ASSET 1: GROWTH COMPARISON (63_exp_2d.png) ---
    plt.figure(figsize=(10, 6))
    plt.plot(t, linear, 'b--', label=r'Linear: $50 + 20t$', lw=2)
    plt.plot(t, exponential, 'r-', label=r'Exponential: $50 \cdot e^{0.4t}$', lw=3)
    
    plt.text(1, 1500, "Exponential Overtakes Linear!", color='darkred', weight='bold')
    plt.title("2D Analysis: Linear vs Exponential Growth Dynamics", fontsize=14)
    plt.xlabel("Time (Steps)"); plt.ylabel("Value / Population")
    plt.grid(alpha=0.3); plt.legend()
    
    plt.savefig(os.path.join(asset_path, '63_exp_2d.png'), dpi=300)
    plt.show()

    # --- 📸 ASSET 2: 3D COMPOUND INTEREST (63_exp_3d.png) ---
    fig = plt.figure(figsize=(12, 9))
    ax3d = fig.add_subplot(111, projection='3d')
    
    time = np.linspace(0, 30, 50)  # 0 to 30 years
    rates = np.linspace(0.01, 0.15, 50) # 1% to 15% interest
    T, R = np.meshgrid(time, rates)
    
    # Final Balance = Principal * e^(rate * time)
    Principal = 1000
    Balance = Principal * np.exp(R * T)

    surf = ax3d.plot_surface(T, R, Balance, cmap='terrain', alpha=0.8)
    
    ax3d.text2D(0.05, 0.85, r"$A = P \cdot e^{rt}$", transform=ax3d.transAxes, 
                fontsize=16, bbox=dict(facecolor='white', alpha=0.7))

    ax3d.set_title("3D Wealth Accumulation: Time vs Interest Rate", fontsize=14)
    ax3d.set_xlabel("Years (t)"); ax3d.set_ylabel("Annual Rate (r)"); ax3d.set_zlabel("Balance ($)")
    fig.colorbar(surf, ax=ax3d, shrink=0.5, aspect=10)
    
    ax3d.view_init(elev=20, azim=-120)
    plt.savefig(os.path.join(asset_path, '63_exp_3d.png'), dpi=300)
    plt.show()

if __name__ == "__main__":
    run_exponential_master()
