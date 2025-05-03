# Re-run the necessary imports and setup due to code execution environment reset
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define different plant systems
def get_plant(system_type):
    if system_type == "Mass-Spring-Damper":
        num = [1]
        den = [1, 2, 1]
    elif system_type == "DC Motor":
        num = [1]
        den = [0.5, 1, 0]
    elif system_type == "First Order Lag":
        num = [1]
        den = [1, 1]
    else:
        num = [1]
        den = [1, 1]
    return ctrl.tf(num, den)

# Simulate the closed-loop system with PID controller
def simulate_system(Kp, Ki, Kd, system_type):
    plant = get_plant(system_type)
    pid = ctrl.tf([Kd, Kp, Ki], [1, 0])
    system = ctrl.feedback(pid * plant, 1)
    t, y = ctrl.step_response(system)
    return t, y

# Update plot based on slider and dropdown values
def update_plot(*args):
    Kp = Kp_var.get()
    Ki = Ki_var.get()
    Kd = Kd_var.get()
    system_type = system_var.get()
    t, y = simulate_system(Kp, Ki, Kd, system_type)

    ax.clear()
    ax.plot(t, y, label=f"{system_type} Step Response")
    ax.set_title("Closed-Loop Step Response")
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Output")
    ax.grid(True)
    ax.legend()
    canvas.draw()

# Set up the main window
root = tk.Tk()
root.title("PID Controller Simulator")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# System selection dropdown
ttk.Label(mainframe, text="Select System").grid(row=0, column=0, sticky=tk.W)
system_var = tk.StringVar(value="Mass-Spring-Damper")
system_menu = ttk.Combobox(mainframe, textvariable=system_var, state="readonly")
system_menu['values'] = ["Mass-Spring-Damper", "DC Motor", "First Order Lag"]
system_menu.grid(row=0, column=1)
system_menu.bind("<<ComboboxSelected>>", update_plot)

# Variables for sliders
Kp_var = tk.DoubleVar(value=1.0)
Ki_var = tk.DoubleVar(value=0.0)
Kd_var = tk.DoubleVar(value=0.0)

# Sliders for PID parameters
ttk.Label(mainframe, text="Kp").grid(row=1, column=0, sticky=tk.W)
ttk.Scale(mainframe, from_=0.0, to=10.0, variable=Kp_var, orient=tk.HORIZONTAL, command=update_plot).grid(row=1, column=1)

ttk.Label(mainframe, text="Ki").grid(row=2, column=0, sticky=tk.W)
ttk.Scale(mainframe, from_=0.0, to=5.0, variable=Ki_var, orient=tk.HORIZONTAL, command=update_plot).grid(row=2, column=1)

ttk.Label(mainframe, text="Kd").grid(row=3, column=0, sticky=tk.W)
ttk.Scale(mainframe, from_=0.0, to=2.0, variable=Kd_var, orient=tk.HORIZONTAL, command=update_plot).grid(row=3, column=1)

# Plotting area
fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=mainframe)
canvas.get_tk_widget().grid(row=4, column=0, columnspan=2)

# Initial plot
update_plot()

root.mainloop()
