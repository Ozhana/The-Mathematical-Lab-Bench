import numpy as np
import matplotlib.pyplot as plt
import os

def run_riemann_analysis():
    f = lambda x: x**2 + 1
    a, b = 0, 2
    n = 15 # Dikdörtgen sayısı
    
    x = np.linspace(a, b, 100)
    y = f(x)
    
    # Riemann noktaları
    x_rect = np.linspace(a, b, n+1)
    y_rect = f(x_rect[:-1]) # Left Riemann Sum
    width = (b - a) / n
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Ana Eğri
    ax.plot(x, y, 'r', lw=3, label='$f(x) = x^2 + 1$')
    
    # Dikdörtgenleri Çizme
    ax.bar(x_rect[:-1], y_rect, width=width, align='edge', 
            alpha=0.3, color='teal', edgecolor='black', label=f'Riemann Sum (n={n})')
    
    # Alan Doldurma (Gerçek Alan)
    ax.fill_between(x, y, alpha=0.1, color='gray')
    
    # Akademik Notasyon
    riemann_sum = np.sum(y_rect * width)
    ax.set_title(f"Lesson 11: Riemann Sum Convergence\nCalculated Area: {riemann_sum:.4f} | Exact: 4.6667", fontsize=14)
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/11_riemann_sums.png')
    plt.show()

if __name__ == "__main__":
    run_riemann_analysis()
