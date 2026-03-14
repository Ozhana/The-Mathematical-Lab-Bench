import numpy as np
import matplotlib.pyplot as plt
import os

def run_optimization():
    # y: river'a dik olan kenar. Maksimum 50 olabilir (50*2=100)
    y = np.linspace(1, 49, 100)
    area = (100 - 2*y) * y
    
    # Sayısal olarak maksimumu bulma
    max_idx = np.argmax(area)
    best_y = y[max_idx]
    best_area = area[max_idx]
    best_x = 100 - 2*best_y

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Alan Fonksiyonu
    ax1.plot(y, area, color='teal', lw=2)
    ax1.scatter(best_y, best_area, color='red', s=100, label=f'Max Area: {best_area}m²')
    ax1.set_title("Area Function: $A(y) = 100y - 2y^2$")
    ax1.set_ylabel("Area ($m^2$)")
    ax1.legend()

    # Değişim Oranı (Türev)
    derivative = 100 - 4*y
    ax2.plot(y, derivative, color='orange', lw=2)
    ax2.axhline(0, color='black', linestyle='--')
    ax2.scatter(best_y, 0, color='red', s=100, label='Derivative = 0')
    ax2.set_title("Rate of Change: $A'(y) = 100 - 4y$")
    ax2.set_xlabel("Side Length y (meters)")
    ax2.legend()

    plt.tight_layout()
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/06_optimization.png')
    plt.show()

if __name__ == "__main__":
    run_optimization()
