# Lesson 14: Area Between Two Curves

### 📗 The Concept
To find the area between two functions $f(x)$ and $g(x)$ over $[a, b]$, we integrate their difference:
$$A = \int_{a}^{b} |f(x) - g(x)| dx$$

### 📝 Example Problem: The Bounded Region
Find the area enclosed by:
1. $f(x) = \sqrt{x}$
2. $g(x) = x^2$
The curves intersect at $(0,0)$ and $(1,1)$.

### 💻 Computational Approach
The script automatically finds intersection points (roots of $f(x) - g(x)$) and shades the region between them. This is a common task in mechanical engineering to find the "cross-section" area of components.

### 📊 Visualization
![Area Between Curves Demo](../../../assets/14_area_between_curves.png)

**Files:**
* `area_solver.py`: Intersection finder and region filler.
* `area_solver.ipynb`: Integral setup and calculation.