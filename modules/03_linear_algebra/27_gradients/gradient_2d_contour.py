import numpy as np
import matplotlib.pyplot as plt
import os

def run_gradient_2d():
    # Fonksiyon: f(x,y) = x*exp(-x^2 - y^2) (Bir tepe ve bir vadi)
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    X, Y = np.meshgrid(x, y)
    Z = X * np.exp(-X**2 - Y**2)
    
    # Gradyan hesaplama (Numerical)
    dy, dx = np.gradient(Z, 0.2, 0.2)
    
    plt.figure(figsize=(10, 8))
    # Kontur haritası
    contour = plt.contourf(X, Y, Z, 20, cmap='RdGy', alpha=0.8)
    plt.colorbar(contour, label='$f(x, y)$ Value')
    
    # Gradyan Vektörleri (Quiver)
    plt.quiver(X, Y, dx, dy, color='blue', alpha=0.6, label='Gradient $\\nabla f$')
    
    plt.title("Lesson 27: 2D Gradient Field (Steepest Ascent)", fontsize=15, fontweight='bold')
    plt.xlabel('x'); plt.ylabel('y')
    plt.legend()
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/27_gradient_2d.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    run_gradient_2d()
