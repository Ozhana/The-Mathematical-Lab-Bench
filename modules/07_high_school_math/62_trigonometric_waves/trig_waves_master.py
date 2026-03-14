import numpy as np
import matplotlib.pyplot as plt
import os

def run_trig_master():
    # --- PROFESSIONAL PATH SETUP ---
    asset_path = r'../../../assets'
    if not os.path.exists(asset_path):
        os.makedirs(asset_path)

    # 1. Generate Wave Data
    x = np.linspace(0, 4 * np.pi, 500)
    wave1 = np.sin(x)            # Frequency 1
    wave2 = np.sin(2.5 * x)      # Frequency 2.5
    interference = wave1 + wave2 # Combined wave

    # --- 📸 ASSET 1: SOUND INTERFERENCE WITH FORMULAS (62_trig_2d.png) ---
    plt.figure(figsize=(12, 7))
    plt.plot(x, wave1, label=r'$y_1 = \sin(x)$ (Base Tone)', alpha=0.4, linestyle='--')
    plt.plot(x, wave2, label=r'$y_2 = \sin(2.5x)$ (High Tone)', alpha=0.4, linestyle='--')
    plt.plot(x, interference, label=r'$Y = y_1 + y_2$ (Resultant)', color='red', lw=2.5)
    
    # Grafik üzerine açıklayıcı metin ekleme
    plt.text(0.5, 1.8, r"Interference: $y = \sin(ax) + \sin(bx)$", fontsize=12, 
             bbox=dict(facecolor='white', alpha=0.8))
    plt.text(7, -1.8, "Constructive & Destructive Interference", color='darkred', weight='bold')

    plt.title("2D Trigonometry: Wave Superposition in Sound Engineering", fontsize=14)
    plt.xlabel("Phase (Radians)"); plt.ylabel("Amplitude (A)")
    plt.grid(alpha=0.3); plt.legend(loc='upper right')
    
    save_path_2d = os.path.join(asset_path, '62_trig_2d.png')
    plt.savefig(save_path_2d, dpi=300)
    print(f"✅ 2D Asset saved: {save_path_2d}")
    plt.show()

    # --- 📸 ASSET 2: 3D SIGNAL DECAY WITH FORMULAS (62_trig_3d.png) ---
    fig = plt.figure(figsize=(12, 9))
    ax3d = fig.add_subplot(111, projection='3d')
    
    t_vals = np.linspace(0, 10, 100)
    x_vals = np.linspace(0, 10, 100)
    T, X = np.meshgrid(t_vals, x_vals)
    
    # Wave Equation with Exponential Decay
    # Z = A * sin(X - T) * e^(-0.2X)
    Z = np.sin(X - T) * np.exp(-0.2 * X)

    surf = ax3d.plot_surface(X, T, Z, cmap='plasma', alpha=0.75, edgecolor='none')
    
    # 3D Grafik üzerine formül ekleme
    ax3d.text(0, 0, 1.5, r"$f(x,t) = \sin(kx - \omega t) \cdot e^{-\alpha x}$", 
              fontsize=14, color='darkblue', weight='bold')
    
    ax3d.set_title("3D Wi-Fi Signal Propagation: Amplitude Decay Over Distance", fontsize=14)
    ax3d.set_xlabel("Distance (x)"); ax3d.set_ylabel("Time (t)"); ax3d.set_zlabel("Signal (A)")
    fig.colorbar(surf, ax=ax3d, shrink=0.5, aspect=10)
    
    ax3d.view_init(elev=25, azim=-45)

    save_path_3d = os.path.join(asset_path, '62_trig_3d.png')
    plt.savefig(save_path_3d, dpi=300)
    print(f"✅ 3D Asset saved: {save_path_3d}")
    plt.show()

if __name__ == "__main__":
    run_trig_master()
