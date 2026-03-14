import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""
The Mathematical Lab Bench: Statistical Inference Engine
Author: Dr. Ozhan Akdag
Description: Ph.D. level automated statistical analysis and visualization.
"""

def perform_statistical_analysis(data_points=1000):
    # 1. Generate Synthetic Data (Normal Distribution)
    # Let's assume this represents sensor error rates or exam scores
    mu, sigma = 50, 15 
    data = np.random.normal(mu, sigma, data_points)

    # 2. Statistical Computations
    mean = np.mean(data)
    std_dev = np.std(data)
    
    print(f"[+] Analysis Complete")
    print(f"    - Mean: {mean:.2f}")
    print(f"    - Std Dev: {std_dev:.2f}")

    # 3. Professional Visualization
    plt.figure(figsize=(12, 7))
    
    # Plot Histogram
    count, bins, ignored = plt.hist(data, 30, density=True, alpha=0.6, color='skyblue', label='Sample Data')
    
    # Plot Probability Density Function (Bell Curve)
    x = np.linspace(min(bins), max(bins), 100)
    plt.plot(x, norm.pdf(x, mean, std_dev), 'r-', lw=2, label='Normal Distribution (Theory)')
    
    # Annotation
    plt.axvline(mean, color='k', linestyle='dashed', linewidth=1, label=f'Mean ({mean:.2f})')
    
    plt.title("Statistical Inference: Gaussian Distribution Analysis", fontsize=16)
    plt.xlabel("Value Range", fontsize=12)
    plt.ylabel("Probability Density", fontsize=12)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    # Save output for GitHub
    plt.savefig('assets/statistical_analysis_demo.png')
    print("[+] Visualization saved to assets/statistical_analysis_demo.png")

if __name__ == "__main__":
    perform_statistical_analysis()
