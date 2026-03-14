import numpy as np
import matplotlib.pyplot as plt
import os

def run_advanced_vector_ops():
    # Temel Vektörler
    a = np.array([4, 1])
    b = np.array([2, 3])
    
    # İzdüşüm (Projection) Hesabı: (a.b / |a|^2) * a
    proj_b_a = (np.dot(a, b) / np.dot(a, a)) * a
    # Dik bileşen (Orthogonal)
    ortho_b_a = b - proj_b_a

    plt.figure(figsize=(10, 10))
    
    # Birim Çember (Uzay ölçeğini hissettirmek için)
    t = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(t), np.sin(t), 'k--', alpha=0.2, label='Unit Circle')

    # Quiver (Oklar) - Daha kalın ve belirgin
    origin = [0], [0]
    plt.quiver(*origin, a[0], a[1], color='#2c3e50', angles='xy', scale_units='xy', scale=1, label='Vector A (Base)')
    plt.quiver(*origin, b[0], b[1], color='#e74c3c', angles='xy', scale_units='xy', scale=1, label='Vector B (Target)')
    plt.quiver(*origin, proj_b_a[0], proj_b_a[1], color='#3498db', angles='xy', scale_units='xy', scale=1, label='Projection of B on A')

    # Dik bileşeni (hata vektörü) çiz
    plt.plot([b[0], proj_b_a[0]], [b[1], proj_b_a[1]], 'k:', lw=2, label='Orthogonal Component')

    plt.xlim(-1, 5); plt.ylim(-1, 5)
    plt.axhline(0, color='black', lw=1.5); plt.axvline(0, color='black', lw=1.5)
    plt.title("Lesson 21: Orthogonal Projection & Vector Decomposition", fontsize=15)
    plt.legend(loc='upper right')
    plt.grid(True, alpha=0.2)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/21_vector_ops.png', dpi=300) # Yüksek kalite
    plt.show()

if __name__ == "__main__":
    run_advanced_vector_ops()
