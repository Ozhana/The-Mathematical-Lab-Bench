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
import scipy.stats as stats
import seaborn as sns
import os

def run_anova_pipeline():
    # Assets yolu
    asset_path = '../../../assets'
    if not os.path.exists(asset_path): os.makedirs(asset_path)

    # 1. Veri Üretimi (3 Farklı Grup)
    np.random.seed(10)
    g1 = np.random.normal(50, 10, 100)
    g2 = np.random.normal(55, 10, 100)
    g3 = np.random.normal(65, 10, 100) # Belirgin şekilde farklı

    f_stat, p_val = stats.f_oneway(g1, g2, g3)

    # --- ASSET 1: 2D VISUALIZATION (Box & Violin) ---
    fig2d = plt.figure(figsize=(10, 8))
    sns.violinplot(data=[g1, g2, g3], palette="light:g", inner="points")
    plt.xticks([0, 1, 2], ['Group A', 'Group B', 'Group C'])
    plt.title(f"ANOVA 2D: Group Comparison\nF-Statistic: {f_stat:.2f} | P-Value: {p_val:.4f}")
    plt.savefig(f'{asset_path}/35_anova_2d.png', dpi=300)
    plt.close(fig2d)

    # --- ASSET 2: 3D VISUALIZATION (Distribution Mountains) ---
    fig3d = plt.figure(figsize=(10, 8))
    ax3d = fig3d.add_subplot(111, projection='3d')
    
    x = np.linspace(20, 100, 100)
    groups = [g1, g2, g3]
    colors = ['r', 'g', 'b']
    
    for i, g in enumerate(groups):
        mu, std = np.mean(g), np.std(g)
        y = stats.norm.pdf(x, mu, std)
        # 3D'de her grubu farklı bir derinliğe (z) yerleştiriyoruz
        ax3d.plot(x, [i]*100, y, color=colors[i], lw=3, label=f'Group {i+1}')
        ax3d.add_collection3d(plt.fill_between(x, 0, y, color=colors[i], alpha=0.2), zs=i, zdir='y')

    ax3d.set_title("3D Variance Landscape: Peak Separation")
    ax3d.set_yticks([0, 1, 2])
    ax3d.set_yticklabels(['A', 'B', 'C'])
    ax3d.legend()
    plt.savefig(f'{asset_path}/35_anova_3d.png', dpi=300)
    plt.close(fig3d)

    # --- MASTER DASHBOARD ---
    master_fig = plt.figure(figsize=(20, 10))
    
    ax_l = master_fig.add_subplot(121)
    sns.boxplot(data=[g1, g2, g3], ax=ax_l)
    ax_l.set_title("Descriptive Summary (2D)")

    ax_r = master_fig.add_subplot(122, projection='3d')
    for i, g in enumerate(groups):
        mu, std = np.mean(g), np.std(g)
        y = stats.norm.pdf(x, mu, std)
        ax_r.plot(x, [i]*100, y, lw=2)
    ax_r.set_title("Distribution Peaks (3D)")

    plt.suptitle(f"Lesson 35: ANOVA Analysis - Decision: {'Significant Difference' if p_val < 0.05 else 'No Significant Difference'}", fontsize=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_anova_pipeline()
