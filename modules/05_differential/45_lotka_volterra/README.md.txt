# Lesson 45: Lotka-Volterra Equations - Coupled Systems

### 📗 The Predator-Prey Equations
This model describes the dynamics of biological systems in which two species interact, one as a predator and the other as prey.

$$\frac{dx}{dt} = \alpha x - \beta xy$$
$$\frac{dy}{dt} = \delta xy - \gamma y$$

### 📊 Visualizing the Ecosystem

#### I. Population Time Series (2D)
This plot shows the oscillating relationship between species. Notice the **phase lag**: the predator population (Red) peaks shortly after the prey population (Blue) peaks.
![Lotka-Volterra 2D](../../../assets/45_lotka_2d.png)

#### II. Phase Space Orbit (3D)
By adding the **Time** axis to the Prey-Predator relationship, we visualize the system's "Limit Cycle" as a 3D trajectory. This shows the recurring nature of the ecosystem's state.
![Lotka-Volterra 3D](../../../assets/45_lotka_3d.png)

---

### 📝 Key Insights
- **Stability:** The system doesn't collapse; it orbits an equilibrium point.
- **Sensitivity:** Small changes in birth/death rates can dramatically change the amplitude of the oscillations.