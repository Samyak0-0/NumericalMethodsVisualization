import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Define function and its derivative
def f(x):
    return np.exp(x) - 4*x

def df(x):
    return np.exp(x) - 4

# Newton-Raphson method to collect iteration steps
def newton_raphson(x0, max_iter=10, tol=1e-6):
    steps = [x0]
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        steps.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return steps

# Compute steps
x0 = 1.0
steps = newton_raphson(x0)
n_steps = len(steps)
current_step = [0]  # use list for mutable int

# Set up plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(bottom=0.2)
x_vals = np.linspace(0, 2.5, 500)
ax.plot(x_vals, f(x_vals), label=r'$f(x) = e^x - 4x$')
ax.axhline(0, color='gray', linestyle='--')

# Plot elements
point, = ax.plot([], [], 'ro', label='Current Point')
tangent_line, = ax.plot([], [], 'g--', lw=1.5, label='Tangent Line')
text_step = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Update plot for given iteration
def update_plot(i):
    if i >= len(steps) - 1:
        i = len(steps) - 2
    elif i < 0:
        i = 0
    x = steps[i]
    y = f(x)
    point.set_data([x], [y])
    
    # Tangent line
    slope = df(x)
    intercept = y - slope * x
    x_tangent = np.linspace(x - 0.5, x + 0.5, 100)
    y_tangent = slope * x_tangent + intercept
    tangent_line.set_data(x_tangent, y_tangent)

    text_step.set_text(f"Iteration {i}: x = {x:.6f}")
    fig.canvas.draw_idle()

update_plot(current_step[0])

# Create buttons
axprev = plt.axes([0.3, 0.05, 0.1, 0.075])
axnext = plt.axes([0.6, 0.05, 0.1, 0.075])
btn_prev = Button(axprev, 'Previous')
btn_next = Button(axnext, 'Next')

# Button callbacks
def prev(event):
    current_step[0] = max(0, current_step[0] - 1)
    update_plot(current_step[0])

def next(event):
    current_step[0] = min(n_steps - 2, current_step[0] + 1)
    update_plot(current_step[0])

btn_prev.on_clicked(prev)
btn_next.on_clicked(next)

# Final plot adjustments
ax.set_title("Newton-Raphson: $e^x = 4x$")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

plt.show()
