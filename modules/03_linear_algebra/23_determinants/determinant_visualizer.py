import numpy as np
import matplotlib.pyplot as plt
import os

def run_determinant_show():
    # Matris tanımı (Dönüştürücü)
    A = np.array([[3, 1], 
                  [0, 2]])
    det_A = np.linalg.det(A)

    # Birim kare noktaları
    square = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0]])
    
    # Dönüştürülmüş paralelkenar
    transformed = A @ square

    plt.figure(figsize=(10, 8))
    
    # Orijinal Kare
    plt.fill(square[0], square[1], color='gray', alpha=0.2, label='Unit Square (Area=1)')
    
    # Dönüştürülmüş Alan
    plt.fill(transformed[0], transformed[1], color='#f1c40f', alpha=0.5, 
             edgecolor='#d35400', lw=3, label=f'Transformed (Area={det_A:.0f})')

    # Vektörleri (okları) belirginleştir
    plt.quiver([0, 0], [0, 0], A[0,:], A[1,:], color=['#e74c3c', '#3498db'], 
               angles='xy', scale_units='xy', scale=1, width=0.015, zorder=5)

    plt.title(f"Lesson 23: Determinant as Area Scaling\n$det(A) = {det_A:.2f}$", fontsize=16)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.axis('equal')
    plt.legend()
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/23_determinant_area.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_determinant_show()
