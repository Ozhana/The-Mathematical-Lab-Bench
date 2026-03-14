# Lesson 05: Mean Value Theorem (MVT)

### 📘 Mathematical Context
The **Mean Value Theorem** states that for a continuous and differentiable function on $[a, b]$, there exists at least one point $c$ in $(a, b)$ such that the instantaneous rate of change (derivative) equals the average rate of change:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### 💻 Computational Approach
We plot a curve and the **secant line** connecting the endpoints. Then, the script algorithmically finds the point $c$ where the **tangent line** is parallel to the secant, providing a visual proof of the theorem.

### 📊 Visualization
![MVT Analysis](../../../assets/05_mvt.png)

**Files in this folder:**
* `mvt_analysis.py`: Standalone Python script.
* `mvt_analysis.ipynb`: Interactive Jupyter Notebook.