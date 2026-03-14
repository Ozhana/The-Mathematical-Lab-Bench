import numpy as np
import matplotlib.pyplot as plt
import os

def run_monte_carlo():
    N = 5000 # Toplam nokta sayısı
    x_rand = np.random.uniform(0, 1, N)
    y_rand = np.random.uniform(0, 1, N)
    
    # Çemberin üst çeyreği: x^2 + y^2 <= 1
    under_curve = x_rand**2 + y_rand**2 <= 1
    pi_estimate = (np.sum(under_curve) / N) * 4

    plt.figure(figsize=(10, 8))
    
    # Noktaları çizme (Altında kalanlar vs Dışında kalanlar)
    plt.scatter(x_rand[under_curve], y_rand[under_curve], color='cyan', s=1, alpha=0.5, label='Inside Area')
    plt.scatter(x_rand[~under_curve], y_rand[~under_curve], color='tomato', s=1, alpha=0.5, label='Outside Area')
    
    # Birim çeyrek çember çizgisini ekle
    theta = np.linspace(0, np.pi/2, 100)
    plt.plot(np.cos(theta), np.sin(theta), color='black', lw=3)

    plt.title(f"Lesson 20: Monte Carlo Estimation of $\pi$\nEstimated Value: {pi_estimate:.5f} (N={N})", fontsize=14)
    plt.legend(markerscale=10)
    plt.axis('equal')
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/20_monte_carlo.png')
    plt.show()

if __name__ == "__main__":
    run_monte_carlo()
