import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os

def run_ibp_analysis():
    x_sym = sp.Symbol('x')
    f_sym = x_sym * sp.exp(-x_sym) # x*e^-x
    
    # Sympy ile sembolik integral çözümü
    integral_sym = sp.integrate(f_sym, x_sym)
    
    # Grafik için fonksiyonlara dönüştürme
    f_num = sp.lambdify(x_sym, f_sym, 'numpy')
    int_num = sp.lambdify(x_sym, integral_sym, 'numpy')
    
    x_vals = np.linspace(0, 5, 200)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, f_num(x_vals), 'b', lw=2, label='Function: $x e^{-x}$')
    plt.plot(x_vals, int_num(x_vals), 'r--', lw=2, label='Integral (via IBP)')
    plt.fill_between(x_vals, f_num(x_vals), alpha=0.2, color='blue')
    
    plt.title(f"Lesson 18: Symbolic Integration by Parts\nSolved: ${sp.latex(integral_sym)}$", fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/18_integration_by_parts.png')
    plt.show()

if __name__ == "__main__":
    run_ibp_analysis()
