import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def run_eigen_show_3d():
    # 3x3 Transformasyon Matrisi (Örn: X-Y'de genişleme, Z'de dönme)
    # A = [[stretch_x, 0, 0], [0, stretch_y, 0], [0, 0, stretch_z]]
    A = np.array([[2.0, 0.0, 0.0],
                  [0.0, 1.5, 0.0],
                  [0.0, 0.0, 0.5]])
    
    # Özdeğer ve Özvektörleri hesapla
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # Nokta Bulutu Oluştur (Bir küre veya küp)
    # Küre noktaları (Spherical coordinates)
    n = 50
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Noktaları birer vektör sütunu yap
    sphere = np.vstack([x.ravel(), y.ravel(), z.ravel()])
    
    # Transformasyon uygula
    transformed_sphere = A @ sphere
    
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # 1. Orijinal Küreyi Çiz (Silik)
    # ax.plot_surface(x, y, z, color='gray', alpha=0.1, edgecolor='none')
    
    # 2. Rastgele Vektörlerin (Noktaların) Dönüşümünü Çiz (Oklar veya Nokta Bulutu)
    # Daha temiz bir görsel için nokta bulutu kullanalım
    ax.scatter(transformed_sphere[0], transformed_sphere[1], transformed_sphere[2], 
               c=transformed_sphere[0], cmap='viridis', alpha=0.2, s=5, label='Transformed Space')

    # 3. ÖZVEKTÖRLERİ ÇİZ (Şovun Yıldızları - Oklar ve Doğrular)
    colors = ['#e74c3c', '#2ecc71', '#3498db'] # Kırmızı, Yeşil, Mavi
    for i in range(len(eigenvalues)):
        ev = eigenvectors[:, i]
        # Gerçek özvektör okunu çiz
        ax.quiver(0, 0, 0, ev[0]*eigenvalues[i]*1.5, ev[1]*eigenvalues[i]*1.5, ev[2]*eigenvalues[i]*1.5, 
                  color=colors[i], lw=3, label=f'Eigenvector {i+1} ($\lambda$={eigenvalues[i]:.2f})', 
                  arrow_length_ratio=0.1)

    # Eksenleri ve Başlığı Ayarla
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_zlim(-3, 3)
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.set_title("Lesson 25: 3D Eigen-decomposition Visualizing Spatial Scaling", fontsize=18)
    ax.legend(loc='upper right', frameon=True, shadow=True, fontsize=12)
    ax.grid(True, alpha=0.2)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/25_eigenvalues_3d.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_eigen_show_3d()
