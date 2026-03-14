# Lesson 29: Optimization - Peaks, Valleys, and Saddles

### 📗 The Second Derivative Test
To find the critical points of a surface $f(x, y)$, we solve $\nabla f = 0$. However, not every critical point is a peak or a valley. We use the **Hessian Determinant ($D$)** to classify them:
- **Local Minimum/Maximum:** The surface curves upwards or downwards in all directions.
- **Saddle Point:** The surface curves up in one direction and down in another (like a Pringles chip).

### 📝 Mathematical Model: The Hyperbolic Paraboloid
We analyze the function $f(x, y) = x^2 - y^2$. 
- At $(0,0)$, the partial derivatives are zero.
- Moving along the x-axis, it looks like a minimum.
- Moving along the y-axis, it looks like a maximum.
This "conflict" creates a **Saddle Point**.

---

### 💻 Computational Approach: The Dual-Asset Engine
Our unified script performs two tasks:
1. **3D Manifold Rendering:** Visualizes the "Saddle" geometry and marks the critical point in 3D space.
2. **2.5D Contour Analysis:** Shows the "Hyperbolic" nature of the level curves around the saddle point.

### 📊 Visual Evidence
We store both perspectives in the `assets` folder to maintain professional documentation standards.

#### I. 3D Saddle Geometry
The "Pringles" shape where the blue paths (descending) and red paths (ascending) meet.
![Saddle Point 3D](../../../assets/29_saddle_3d.png)


#### II. 2D Hyperbolic Contours
Note how the contour lines flip their orientation at the origin, a classic signature of a saddle point.
![Saddle Point 2D](../../../assets/29_saddle_2d.png)


**Files:**
* `saddle_point_master.py`: Unified engine generating dual assets.