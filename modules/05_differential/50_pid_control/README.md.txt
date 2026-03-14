# Lesson 50: PID Control - The Grand Finale of Stage 5

### 📗 The Control Law
A PID controller continuously calculates an error value $e(t)$ as the difference between a desired setpoint and a measured process variable:
$$u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

- **Proportional (P):** Corrects based on current error.
- **Integral (I):** Corrects based on accumulated past errors (eliminates steady-state error).
- **Derivative (D):** Corrects based on the predicted future error (dampens oscillations).

---

### 📊 Visualizing the Controller's Performance

#### I. Step Response (2D)
The battle between the controller and physics. We see how the system reaches the target (setpoint), handles overshoot, and finally settles into stability.
![PID Control step response curve](../../../assets/50_pid_2d.png)

#### II. Error Surface & Parameter Tuning (3D)
A 3D landscape showing the **Total Settling Error** as a function of $K_p$ and $K_d$. We are looking for the "valley" - the optimal parameters for the perfect controller.
![PID Control parameter optimization 3D](../../../assets/50_pid_3d.png)