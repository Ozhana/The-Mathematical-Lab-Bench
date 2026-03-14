import numpy as np
import matplotlib.pyplot as plt
import os

def run_mvt_analysis():
    f = lambda x: 0.5*x**3 - 2*x + 2
    df = lambda x: 1.5*x**2 - 2
    
    a, b = -1, 2
    x = np.linspace(-1.5, 2.5, 100)
    
    # Average slope (Secant)
    m_secant = (f(b) - f(a)) / (b - a)
    
    # Find c where f'(c) = m_secant using quadratic formula for this specific df
    # 1.5c^2 - 2 = m_secant => c = sqrt((m_secant + 2) / 1.5)
    c = np.sqrt((m_secant + 2) / 1.5) # Taking the positive root in [a,b]

    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), 'k', lw=2, label='f(x)')
    
    # Plot Secant Line
    plt.plot([a, b], [f(a), f(b)], 'b--', marker='o', label='Secant (Avg Change)')
    
    # Plot Tangent at c
    tangent_x = np.linspace(c-0.5, c+0.5, 20)
    tangent_y = m_secant*(tangent_x - c) + f(c)
    plt.plot(tangent_x, tangent_y, 'r', lw=2, label=f'Parallel Tangent at c={c:.2f}')
    plt.scatter([c], [f(c)], color='red')

    plt.title("Lesson 05: Visualizing Mean Value Theorem", fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists('../../../assets'):
        os.makedirs('../../../assets')
    plt.savefig('../../../assets/05_mvt.png')
    plt.show()

if __name__ == "__main__":
    run_mvt_analysis()
