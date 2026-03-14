# Lesson 24: Gaussian Elimination & Row Echelon Form

### 📗 Theoretical Framework
Gaussian Elimination is the fundamental algorithm for solving systems of linear equations ($Ax = b$). It uses elementary row operations to transform a matrix into an **Upper Triangular** form.

### 📝 The Engineering Core: Forward Elimination
For any robotic system (like your Arduino-based control loops), solving state equations requires this step. We focus on:
1. **Pivoting:** Selecting the largest element to maintain numerical stability.
2. **Back Substitution:** Finding the variables once the matrix is triangular.

### 💻 Computational Approach
Instead of just showing the result, we visualize the **Matrix Evolution**. Using a heatmap, we show how the coefficients "vanish" (become zero) below the pivot, moving the system toward a solution.

### 📊 Visualization
![Gaussian Elimination Steps Demo](../../../assets/24_gaussian_elimination.png)