# Lesson 18: Integration by Parts (IBP)

### 📗 Theoretical Framework
Integration by Parts is the integral counterpart of the product rule for derivatives. It is defined by the formula:
$$\int u \, dv = uv - \int v \, du$$
This is the "Golden Key" for integrating products of algebraic and transcendental functions (e.g., $x \cdot e^x$ or $x \cdot \sin(x)$).

### 📝 Example Problem: $x \cdot \ln(x)$
Find $\int x \ln(x) dx$ on $[1, e]$.
1. Let $u = \ln(x) \implies du = \frac{1}{x} dx$
2. Let $dv = x dx \implies v = \frac{x^2}{2}$
3. Solution: $\frac{x^2}{2}\ln(x) - \int \frac{x}{2} dx = \frac{x^2}{2}\ln(x) - \frac{x^2}{4}$.

### 💻 Computational Approach
In this lesson, we introduce **Symbolic Computation** using the `sympy` library. This allows the computer to "understand" the algebraic steps of IBP, solve the integral exactly, and then plot the result.

### 📊 Visualization
![IBP Demo](../../../assets/18_integration_by_parts.png)