# Lesson 28: Partial Derivatives & The Tangent Plane

### 📗 The Logic of Slicing
Partial derivatives ($\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$) are the slopes of a surface when we slice it along the $x$ or $y$ axis. They answer the question: "How does the height change if I only move in one direction?"

### 📝 The Tangent Plane: Linear Approximation
Just as a 1D function has a tangent line, a 2D surface has a **Tangent Plane**. At any point $(a, b)$, the equation of the plane is:
$$z - f(a,b) = f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
This plane is the "Best Linear Approximation" of the surface at that point.

---

### 💻 Computational Approach: The Unified Visualizer
In this lesson, we break the boundaries and combine 2D and 3D perspectives into a single unified dashboard:
1.  **Left Subplot (3D):** The surface with the Tangent Plane "touching" it at a specific point.
2.  **Right Subplot (2D):** A "Slice Analysis" showing the specific partial derivative curve.

### 📊 Visual Evidence
![Tangent Plane Analysis](../../../assets/28_tangent_plane.png)


**Files:**
* `partial_deriv_master.py`: The unified 2D/3D visualization engine.