import numpy as np
import matplotlib.pyplot as plt
import os

def run_derivative_analysis():
    f = lambda x: x**2
    df = lambda x: 2*x # f(x)'in türevi

    x = np.linspace(-2, 2, 100)
    p = 1.0 # Teğet noktası
    
    # Teğet doğrusu denklemi
    tangent_x = np.linspace(0.5, 1.5, 20)
    tangent_y = df(p)*(tangent_x - p) + f(p)

    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), 'k', lw=2, label='f(x) = x²')
    plt.plot(tangent_x, tangent_y, 'r--', lw=2, label=f'Tangent at x={p} (Slope={df(p)})')
    plt.scatter([p], [f(p)], color='red', s=80, zorder=5)

    plt.title("Lesson 03: Geometric Interpretation of Derivatives", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    if not os.path.exists('../../../assets'):
        os.makedirs('../../../assets')
    plt.savefig('../../../assets/03_derivative_slope.png')
    plt.show()

if __name__ == "__main__":
    run_derivative_analysis()
