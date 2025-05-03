# PID Controller Simulator

This is a small GUI application built in Python that allows users to experiment with **PID controllers** on different system models. It helps visualize how **Proportional (P)**, **Integral (I)**, and **Derivative (D)** gains affect the **step response** of common systems.

---

## 📌 Features

- Interactive sliders for:
  - Proportional Gain (Kp)
  - Integral Gain (Ki)
  - Derivative Gain (Kd)
-Dropdown menu to select one of the following systems:
  - Mass-Spring-Damper
  - DC Motor
  - First Order Lag System
- Live step response plotting with automatic updates

---

## ⚙️ PID Controller Overview
A **PID controller** is a widely used feedback mechanism in control systems. It adjusts the control input based on three components:

- **Proportional (P)**: Reacts to the current error $e(t)$.
- **Integral (I)**: Reacts to the accumulated error over time.
- **Derivative (D)**: Reacts to the rate of change of the error.

The controller output $u(t)$ is given by:

$$
u(t) = K_p \cdot e(t) + K_i \int e(t) \, dt + K_d \cdot \frac{de(t)}{dt}
$$

Where:

- $K_p$: proportional gain
- $K_i$: integral gain
- $K_d$: derivative gain
- $e(t)$: the error between desired and actual output

---

## 🏗️ System Types Modeled

### 1. Mass-Spring-Damper System
Represents mechanical systems such as suspensions or robotic arms.

**Transfer Function**:

$$
G(s) = \frac{1}{s^2 + 2s + 1}
$$

**Behaviour**: Oscillatory, second-order dynamics with damping.

### 2. DC Motor
Models electric motor speed or position control.

**Transfer Function**:

$$
G(s) = \frac{1}{0.5s^2 + s}
$$

**Behaviour**: Moderate overshoot, slower due to inertia.

### 3. First Order Lag System
A simple dynamic system with single energy storage.

**Transfer Function**:

$$
G(s) = \frac{1}{s+1}
$$

**Behaviour**: Smooth, slow response without oscillations.

---

## 📦 Requirements
Install the required Python libraries:
```bash
pip install numpy matplotlib control tkinter
```

---

## ▶️ How to Run
Simply run the Python script:
```bash
python PIDControllerSimulator.py
```
The GUI will open with sliders and a dropdown menu. Adjust the PID values and observe how the system response changes.
