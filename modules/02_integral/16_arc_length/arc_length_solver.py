import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import os

def run_arc_length_analysis():
    # f(x) = sin(x)
    f = lambda x: np.sin(x)
    df = lambda x: np.cos(x) # Türevi
    
    a, b = 0, np.pi
    x = np.linspace(a, b, 100)
    
    # Yay Uzunluğu İntegrali: sqrt(1 + f'(x)^2)
    integrand = lambda x: np.sqrt(1 + df(x)**2)
    length, error = quad(integrand, a, b)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), 'b-', lw=3, label=f'Curve: $\sin(x)$')
    
    # Yay uzunluğu illüstrasyonu (Küçük segmentler)
    plt.fill_between(x, f(x), alpha=0.1, color='blue')
    
    plt.title(f"Lesson 16: Arc Length Analysis\nTotal Calculated Length: {length:.5f}", fontsize=14)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/16_arc_length.png')
    plt.show()

if __name__ == "__main__":
    run_arc_length_analysis()
