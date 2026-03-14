import numpy as np
import matplotlib.pyplot as plt
import os

def run_lhopital():
    x = np.linspace(-5, 5, 500)
    # Using small epsilon to avoid true division by zero
    y = np.sin(x) / x 
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color='crimson', lw=2, label=r'$f(x) = \frac{\sin(x)}{x}$')
    
    # Highlight the limit point
    plt.scatter([0], [1], color='black', s=100, zorder=5, label='Limit Value = 1')
    
    plt.axhline(1, color='gray', linestyle='--', alpha=0.5)
    plt.title("Lesson 09: L'Hopital's Rule Visualization", fontsize=14)
    plt.xlabel("x")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/09_lhopital.png')
    plt.show()

if __name__ == "__main__":
    run_lhopital()
