# Lesson 08: Taylor Series Expansion

### 📗 What is a Taylor Series?
Taylor Series is a way to represent a function (like $\sin(x)$ or $e^x$) as an **infinite sum of polynomials**. In computing, this is how calculators and computers actually calculate trigonometric values.

**General Formula:**
$$f(x) \approx \sum_{n=0}^{N} \frac{f^{(n)}(a)}{n!}(x-a)^n$$

### 📝 Example: Approximating $\sin(x)$
How many polynomial terms do we need to accurately represent a wave? 
- 1st Order: $x$ (Linear)
- 3rd Order: $x - \frac{x^3}{3!}$ (Cubic)
- 5th Order: $x - \frac{x^3}{3!} + \frac{x^5}{5!}$ (Quintic)

### 💻 Computational Approach
The script calculates these polynomials and overlays them on the actual function. This demonstrates **convergence**: as the order increases, the polynomial "clings" to the function over a wider range.

### 📊 Visualization
![Taylor Series Demo](../../../assets/08_taylor_series.png)

**Files:**
* `taylor_solver.py`: Generates polynomial approximations.
* `taylor_solver.ipynb`: Detailed step-by-step breakdown.