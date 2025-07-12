import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Define function and its derivative
def f(x):
    return np.exp(x) - 4*x

def df(x):
    return np.exp(x) - 4

# Newton-Raphson method to collect steps
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
current_step = [0]  # mutable integer

# Set up plot
fig, ax = plt.subplots(figsize=(9, 6))
plt.subplots_adjust(bottom=0.25)
x_vals = np.linspace(0, 2.5, 500)
ax.plot(x_vals, f(x_vals), label=r'$f(x) = e^x - 4x$')
ax.axhline(0, color='black', linestyle='--', linewidth=0.7)

# Plot elements
point, = ax.plot([], [], 'ro', label='Current Point')
tangent_line, = ax.plot([], [], 'g--', lw=1.5, label='Tangent Line')
vertical_to_curve, = ax.plot([], [], 'b:', lw=1)
x_intercept_marker, = ax.plot([], [], 'ko', label='Root Approx.')
text_step = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Update plot per iteration
def update_plot(i):
    if i >= len(steps) - 1:
        i = len(steps) - 2
    elif i < 0:
        i = 0

    x_n = steps[i]
    y_n = f(x_n)
    point.set_data([x_n], [y_n])

    # Tangent line at x_n
    slope = df(x_n)
    intercept = y_n - slope * x_n

    # Compute x-intercept (root approximation)
    if slope != 0:
        x_next = x_n - f(x_n) / slope
    else:
        x_next = x_n

    # Tangent line range
    x_tangent = np.linspace(x_n - 0.75, x_next + 0.75, 100)
    y_tangent = slope * x_tangent + intercept
    tangent_line.set_data(x_tangent, y_tangent)

    # x-intercept marker (where tangent crosses x-axis)
    x_intercept_marker.set_data([x_next], [0])

    # Vertical line from x-intercept up to curve
    y_next = f(x_next)
    vertical_to_curve.set_data([x_next, x_next], [0, y_next])

    text_step.set_text(f"Iteration {i}: x = {x_n:.6f}")
    fig.canvas.draw_idle()

# Initial draw
update_plot(current_step[0])

# Buttons
axprev = plt.axes([0.3, 0.1, 0.1, 0.07])
axnext = plt.axes([0.6, 0.1, 0.1, 0.07])
btn_prev = Button(axprev, 'Previous')
btn_next = Button(axnext, 'Next')

def prev(event):
    current_step[0] = max(0, current_step[0] - 1)
    update_plot(current_step[0])

def next(event):
    current_step[0] = min(n_steps - 2, current_step[0] + 1)
    update_plot(current_step[0])

btn_prev.on_clicked(prev)
btn_next.on_clicked(next)

# Final plot settings
ax.set_title("Newton-Raphson Visualization with Tangents and Projections")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)

plt.show()
