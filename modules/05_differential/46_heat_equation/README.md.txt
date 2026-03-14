# Lesson 46: 1D Heat Equation - Modeling Thermal Diffusion

### 📗 The Partial Differential Equation (PDE)
The heat equation describes how heat spreads through a material over time. In 1D:
$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$
- **$u(x, t)$:** Temperature at position $x$ and time $t$.
- **$\alpha$:** Thermal diffusivity constant.
- **$\frac{\partial^2 u}{\partial x^2}$:** The curvature of the temperature profile (Laplacian).

### 📝 Physical Interpretation
Heat flows from hotter regions to colder regions at a rate proportional to the local temperature gradient's curvature. Over time, the temperature distribution "flattens" out.

---

### 📊 Visualizing Heat Diffusion

#### I. Temperature Evolution (2D)
This plot shows snapshots of the temperature along the rod at different time intervals. Notice how the sharp initial peak gradually smooths out and spreads.
![Heat Equation 2D](../../../assets/46_heat_2d.png)

#### II. Space-Time Heat Map (3D)
A 3D surface where the X-axis is position, the Y-axis is time, and the Z-axis (height) is temperature. This visualizes the entire cooling/heating process as a landscape.
![Heat Equation 3D](../../../assets/46_heat_3d.png)