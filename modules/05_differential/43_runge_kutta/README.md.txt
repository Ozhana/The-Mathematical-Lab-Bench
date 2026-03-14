# Lesson 43: Runge-Kutta (RK4) - The Gold Standard

### 📗 The Logic of RK4
While Euler's method uses only the derivative at the beginning of the interval, **RK4** calculates four different slopes ($k_1, k_2, k_3, k_4$) and takes a weighted average:
1. **$k_1$:** Slope at the beginning.
2. **$k_2$:** Slope at the midpoint (using $k_1$).
3. **$k_3$:** Slope at the midpoint (using $k_2$).
4. **$k_4$:** Slope at the end (using $k_3$).

### 📝 The Mathematical Weighting
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$
This cancels out errors up to the fourth order, making it incredibly stable.

---

### 💻 Computational Approach: The Precision Engine
1. **2D Perspective:** A direct comparison: **Euler vs. RK4 vs. Exact**. You will see RK4 hugging the exact solution while Euler drifts away.
2. **3D Perspective:** **Convergence Landscape**. Visualizing how the error drops drastically as we switch from Euler to RK4 across different step sizes.
3. **Master Dashboard:** Step-by-step weight visualization.

### 📊 Visual Evidence

#### I. 2D Accuracy Comparison
Notice that RK4 (green) is almost indistinguishable from the Exact solution (blue), even with large steps.
![Runge-Kutta vs Euler vs Exact](../../../assets/43_rk4_2d.png)


#### II. 3D Precision Map
A 3D surface showing the "Error Floor." RK4's error is so small it creates a flat valley compared to Euler's mountains of error.
![RK4 3D Error Floor](../../../assets/43_rk4_3d.png)

**Files:**
* `rk4_master.py`: High-precision solver and asset generator.