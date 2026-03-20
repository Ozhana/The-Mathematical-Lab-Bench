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
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import os

def run_correlation_master():
    # --- YOL AYARI (Ph.D. Disiplini) ---
    asset_path = r'../../../assets'
    if not os.path.exists(asset_path):
        os.makedirs(asset_path)

    # 1. Veri Üretimi (Sentetik bir Veri Seti: 5 Değişkenli)
    np.random.seed(42)
    n = 100
    x1 = np.random.randn(n)
    x2 = x1 + np.random.normal(0, 0.5, n) # Güçlü Pozitif
    x3 = -x1 + np.random.normal(0, 0.8, n) # Negatif
    x4 = np.random.randn(n) # Alakasız (Gürültü)
    x5 = 0.5 * x2 + np.random.normal(0, 0.2, n) # Orta Pozitif

    df = pd.DataFrame({'Var_A': x1, 'Var_B': x2, 'Var_C': x3, 'Var_D': x4, 'Var_E': x5})
    corr_matrix = df.corr()

    # --- 📸 ASSET 1: SADECE 2D GRAFİK (37_corr_2d.png) ---
    fig2d = plt.figure(figsize=(10, 8))
    ax2d = fig2d.add_subplot(111)
    
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", 
                linewidths=0.5, vmin=-1, vmax=1, center=0, ax=ax2d)
    ax2d.set_title("2D Correlation Matrix (Pearson $r$)")
    
    plt.savefig(os.path.join(asset_path, '37_corr_2d.png'), dpi=300)
    print(f"✅ 2D Asset kaydedildi: {asset_path}\\37_corr_2d.png")
    plt.close(fig2d)

    # --- 📸 ASSET 2: SADECE 3D GRAFİK (37_corr_3d.png) ---
    fig3d = plt.figure(figsize=(10, 8))
    ax3d = fig3d.add_subplot(111, projection='3d')
    
    # Matrisi 3D koordinatlara çevirme
    size = len(corr_matrix)
    x_pos, y_pos = np.meshgrid(np.arange(size), np.arange(size))
    x_pos = x_pos.flatten()
    y_pos = y_pos.flatten()
    z_pos = np.zeros(size * size)
    
    dx = dy = 0.6
    dz = corr_matrix.values.flatten()

    # Renk haritası (Z değerine göre)
    colors = plt.cm.coolwarm((dz + 1) / 2)

    ax3d.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, alpha=0.8)
    
    ax3d.set_xticks(np.arange(size))
    ax3d.set_xticklabels(df.columns)
    ax3d.set_yticks(np.arange(size))
    ax3d.set_yticklabels(df.columns)
    ax3d.set_title("3D Correlation Topography")
    ax3d.set_zlabel('Correlation Intensity')
    
    plt.savefig(os.path.join(asset_path, '37_corr_3d.png'), dpi=300)
    print(f"✅ 3D Asset kaydedildi: {asset_path}\\37_corr_3d.png")
    plt.close(fig3d)

    # --- 🖥️ DASHBOARD (Preview) ---
    fig_dash = plt.figure(figsize=(20, 10))
    
    ax1 = fig_dash.add_subplot(121)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', cbar=False, ax=ax1)
    ax1.set_title("Matrix View")

    ax2 = fig_dash.add_subplot(122, projection='3d')
    ax2.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors)
    ax2.set_title("Topographic View")

    plt.suptitle("Lesson 37: Multi-Variable Correlation Analysis", fontsize=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_correlation_master()
