import numpy as np
import matplotlib.pyplot as plt
import os

def run_transformation():
    # Bir ızgara (grid) oluşturma
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)
    
    # Izgara noktalarını birer vektör sütunu haline getirme
    points = np.vstack([X.ravel(), Y.ravel()])
    
    # Transformasyon Matrisi (Shear + Scale)
    A = np.array([[1, 1.2], 
                  [0, 1]])
    
    # Tüm noktaları aynı anda dönüştür (Matrix Multiplication)
    transformed_points = A @ points
    
    X_trans = transformed_points[0, :].reshape(X.shape)
    Y_trans = transformed_points[1, :].reshape(Y.shape)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # Orijinal Uzay
    ax1.scatter(X, Y, color='gray', alpha=0.3)
    ax1.plot(X, Y, 'b', alpha=0.2)
    ax1.plot(X.T, Y.T, 'b', alpha=0.2)
    ax1.set_title("Original Identity Space ($I$)")
    ax1.set_xlim(-4, 4); ax1.set_ylim(-4, 4)

    # Dönüştürülmüş Uzay
    ax2.scatter(X_trans, Y_trans, color='red', alpha=0.5)
    ax2.plot(X_trans, Y_trans, 'r', alpha=0.3)
    ax2.plot(X_trans.T, Y_trans.T, 'r', alpha=0.3)
    ax2.set_title("Transformed Space (Matrix $A$)")
    ax2.set_xlim(-4, 4); ax2.set_ylim(-4, 4)

    plt.suptitle("Lesson 22: Linear Transformations as Grid Warping", fontsize=16)
    
    if not os.path.exists('../../../assets'): os.makedirs('../../../assets')
    plt.savefig('../../../assets/22_matrix_transform.png')
    plt.show()

if __name__ == "__main__":
    run_transformation()
