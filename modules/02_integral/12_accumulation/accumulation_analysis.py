import numpy as np
import matplotlib.pyplot as plt
import os

def run_accumulation():
    x = np.linspace(0, 2*np.pi, 200)
    f = np.sin(x)
    
    # Accumulation (Integral of sin is -cos)
    # Using np.cumsum for numerical accumulation
    dx = x[1] - x[0]
    accumulation = np.cumsum(f) * dx
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # Rate Function
    ax1.plot(x, f, color='blue', lw=2, label='Rate $f(t) = \sin(t)$')
    ax1.fill_between(x, f, color='blue', alpha=0.2)
    ax1.axhline(0, color='black', lw=1)
    ax1.set_title("Instantaneous Rate of Change")
    ax1.legend()
    
    # Accumulation Function
    ax2.plot(x, accumulation, color='darkred', lw=2, label='Accumulated Area $F(x)$')
    ax2.set_title("Total Accumulated Area (The Integral)")
    ax2.legend()
    
    plt.tight_layout()
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/12_accumulation.png')
    plt.show()

if __name__ == "__main__":
    run_accumulation()
