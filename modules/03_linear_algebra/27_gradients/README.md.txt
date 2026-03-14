# Lesson 27: Multivariable Landscapes & The Gradient Vector

### 📗 The Geometry of Change
In single-variable calculus, the derivative gives us the slope of a line. In multivariable calculus, we deal with **Surfaces**. The **Gradient** ($\nabla f$) is a vector that points in the direction of the steepest ascent at any given point.

$$\nabla f(x, y) = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$$

### 📝 Why it Matters? (The Ph.D. Perspective)
- **Gradient Descent:** This is the heart of Machine Learning. To "train" a model, we find the gradient of an error function and move in the opposite direction to find the minimum.
- **Physics:** Gradients define how heat flows (from hot to cold) and how fluids move under pressure.

---

### 💻 Computational Approach
To achieve a "visual feast," we visualize a complex surface (like a saddle or a peak) using two complementary methods:
* `gradient_2d_contour.py`: A top-down heat map with **quiver arrows** showing the direction of the steepest climb at every point.
* `gradient_3d_surface.py`: A 3D mesh rendering where we place a "ball" on the surface and show its path as it follows the gradient.

### 📊 Visual Evidence

#### I. 2.5D Contour Map (The Navigator's View)
The arrows point towards the peaks. This is exactly how an optimizer "sees" the loss landscape in AI.
![Gradient Contour Map](../../../assets/27_gradient_2d.png)


#### II. 3D Surface Analysis (The Topographic View)
Visualizing the partial derivatives as slopes along the $x$ and $y$ cross-sections.
![Gradient 3D Surface](../../../assets/27_gradient_3d.png)


**Files:**
* `gradient_2d_contour.py`: Heatmap & Vector Field engine.
* `gradient_3d_surface.py`: 3D Surface & Tangent Plane simulator.