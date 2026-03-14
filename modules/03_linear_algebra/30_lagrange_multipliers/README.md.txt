# Lesson 30: Lagrange Multipliers - Optimization under Constraints

### 📗 The Geometry of Constraints
In real-world problems, we rarely optimize without limits. Whether it's a budget in economics or a physical boundary in robotics, we seek to maximize $f(x, y)$ subject to a constraint $g(x, y) = k$. 

The core insight of **Joseph-Louis Lagrange** was that the maximum occurs where the gradient of the function is parallel to the gradient of the constraint:
$$\nabla f = \lambda \nabla g$$
Here, $\lambda$ is the **Lagrange Multiplier**, representing the "shadow price" or sensitivity of the optimal value to the constraint.

### 📝 Mathematical Case Study
Find the maximum of $f(x, y) = x + y$ (a tilted plane) subject to the circular constraint $g(x, y) = x^2 + y^2 = 1$. 
- Sezgisel olarak: Bu, bir silindir ile bir düzlemin kesiştiği en yüksek noktayı bulmaktır.

---

### 💻 Computational Approach: The Dual-Asset Engine
This script visualizes the delicate touch between a function's level curves and the constraint boundary:
1. **3D Perspective:** Visualizes the "Intersection Curve" where the plane meets the cylinder.
2. **2D Perspective:** Shows the "Gradient Alignment" ($\nabla f$ and $\nabla g$) at the optimal points.

### 📊 Visual Evidence

#### I. 3D Constrained Surface
The optimization "path" is restricted to the boundary of the constraint.
![Lagrange 3D Visualization](../../../assets/30_lagrange_3d.png)


#### II. 2D Gradient Alignment
The "Sweet Spot" where the contour of $f$ is perfectly tangent to the constraint $g$.
![Lagrange 2D Visualization](../../../assets/30_lagrange_2d.png)


**Files:**
* `lagrange_master.py`: Unified engine for constrained optimization and asset generation.