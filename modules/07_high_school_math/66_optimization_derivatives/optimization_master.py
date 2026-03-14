import numpy as np
import matplotlib.pyplot as plt
import os

def run_optimization_master():
    asset_path = r'../../../assets'
    if not os.path.exists(asset_path): os.makedirs(asset_path)

    # 1. Define Profit Function: P(x) = -2x^2 + 80x - 200
    # Derivative: P'(x) = -4x + 80
    # Peak at x = 20
    x = np.linspace(0, 40, 100)
    profit = -2*x**2 + 80*x - 200
    derivative = -4*x + 80

    # --- 📸 ASSET 1: PROFIT VS DERIVATIVE (66_opt_2d.png) ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), sharex=True)
    
    ax1.plot(x, profit, color='#2c3e50', lw=3, label=r'Profit $P(x)$')
    ax1.scatter([20], [600], color='red', s=100, zorder=5)
    ax1.annotate('Maximum Profit!', xy=(20, 600), xytext=(25, 550),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    ax1.set_ylabel("Profit ($)"); ax1.legend(); ax1.grid(alpha=0.3)
    
    ax2.plot(x, derivative, color='#e67e22', lw=2, label=r"Derivative $P'(x)$ (Slope)")
    ax2.axhline(0, color='black', lw=1)
    ax2.scatter([20], [0], color='red', s=100)
    ax2.set_ylabel("Slope Rate"); ax2.set_xlabel("Units Sold / Price"); ax2.legend(); ax2.grid(alpha=0.3)
    
    plt.suptitle("2D Optimization: Finding the Peak where Slope = 0", fontsize=14)
    plt.savefig(os.path.join(asset_path, '66_opt_2d.png'), dpi=300)
    plt.show()

    # --- 📸 ASSET 2: PROFIT LANDSCAPE (66_opt_3d.png) ---
    fig3d = plt.figure(figsize=(12, 9))
    ax3d = fig3d.add_subplot(111, projection='3d')
    
    x_prod = np.linspace(5, 35, 50) # Production Volume
    y_price = np.linspace(10, 100, 50) # Price Point
    X, Y = np.meshgrid(x_prod, y_price)
    
    # A hypothetical 3D Profit Surface
    Z_profit = -(X-20)**2 - 0.5*(Y-50)**2 + 5000 

    surf = ax3d.plot_surface(X, Y, Z_profit, cmap='viridis', alpha=0.8)
    
    ax3d.set_title("3D Profit Landscape: Optimizing Volume and Price", fontsize=14)
    ax3d.set_xlabel("Production Vol (x)"); ax3d.set_ylabel("Price (y)"); ax3d.set_zlabel("Profit ($)")
    fig3d.colorbar(surf, ax=ax3d, shrink=0.5, aspect=10)
    
    ax3d.view_init(elev=25, azim=135)
    plt.savefig(os.path.join(asset_path, '66_opt_3d.png'), dpi=300)
    plt.show()

if __name__ == "__main__":
    run_optimization_master()
