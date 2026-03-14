import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def run_gradient_3d():
    x = np.linspace(-2, 2, 50)
    y = np.linspace(-2, 2, 50)
    X, Y = np.meshgrid(x, y)
    Z = X * np.exp(-X**2 - Y**2)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Yüzey çizimi
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)
    
    # Estetik dokunuş: İzdüşüm (Contour projection on Z-axis)
    ax.contour(X, Y, Z, zdir='z', offset=np.min(Z)-0.2, cmap='viridis', alpha=0.5)

    ax.set_title("Lesson 27: 3D Scalar Field Visualization", fontsize=16)
    ax.set_zlim(np.min(Z)-0.2, np.max(Z)+0.2)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/27_gradient_3d.png', dpi=300)
    ax.view_init(elev=30, azim=45) # Bakış açısını ayarla
    plt.show()

if __name__ == "__main__":
    run_gradient_3d()
