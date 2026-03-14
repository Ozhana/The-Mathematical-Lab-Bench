import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def run_volume_rotation():
    x = np.linspace(0, 4, 100)
    y = np.sqrt(x)
    
    # 3D Dönüş yüzeyini oluşturma
    angle = np.linspace(0, 2*np.pi, 100)
    X, T = np.meshgrid(x, angle)
    Y = np.sqrt(X) * np.cos(T)
    Z = np.sqrt(X) * np.sin(T)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Yüzey çizimi
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7, edgecolor='none')
    
    # Ana eğriyi vurgula
    ax.plot(x, y, zs=0, zdir='z', color='red', lw=3, label='Original $y=\sqrt{x}$')
    
    ax.set_title("Lesson 15: 3D Volume of Revolution (Disk Method)", fontsize=15)
    ax.set_xlabel("X (Axis of Rotation)")
    plt.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/15_volume_revolution.png')
    plt.show()

if __name__ == "__main__":
    run_volume_rotation()
