# Lesson 20: Monte Carlo Integration & Probabilistic Calculus

### 📗 Theoretical Framework
What if a function is so complex that traditional integration fails? We use the **Monte Carlo Method**. By generating thousands of random points in a bounding box, we estimate the area based on the ratio of points that "land" under the curve.

### 📝 The Experiment: Estimating $\pi$ via Integration
We integrate the upper quadrant of a unit circle: $f(x) = \sqrt{1 - x^2}$ from $0$ to $1$.
The exact area is $\pi/4$. 
- **Method:** Throw $N$ random darts. 
- **Formula:** $\text{Area} \approx \frac{\text{Points Under Curve}}{\text{Total Points}} \times \text{Bounding Box Area}$.

### 💻 Computational Approach
The script visualizes every single "dart throw" (random point). Points under the curve are colored differently. This demonstrates how **Stochastic Processes** can solve deterministic mathematical problems.

### 📊 Visualization
![Monte Carlo Demo](../../../assets/20_monte_carlo.png)