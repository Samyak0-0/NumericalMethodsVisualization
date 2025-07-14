import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


def f(x):
    return np.exp(x) - 4*x

def df(x):
    return np.exp(x) - 4

print("--------------------------------------------------------------------------")
print("iter     Xn           Xn+1           f(X)")
print("--------------------------------------------------------------------------")

steps = None

def newton_raphson(x0, max_iter=15, tol=1e-4):
    steps = [x0]
    for _ in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        print(f" {_}     {x0:.4f}        {x1:.4f}         {f(x0):.4f}")
        steps.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return steps


x0 = 1.0
steps = newton_raphson(x0)
n_steps = len(steps)
current_step = [0]
print(f"\nThe root of the equation f(X) = e^x - 4x = 0 is {steps[-1]:.4f}.")

# Plot Section
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

    slope = df(x_n)
    x_next = x_n - f(x_n) / slope if slope != 0 else x_n
    y_next = f(x_next)

    # Extended tangent line around (x_n, f(x_n)) to (x_next, 0)
    dx = x_next - x_n
    pad = 0.2
    x_start = x_n - pad * dx
    x_end = x_next + pad * dx
    x_tangent = np.linspace(x_start, x_end, 100)
    y_tangent = y_n + slope * (x_tangent - x_n)
    tangent_line.set_data(x_tangent, y_tangent)

    # Vertical and intercept marker
    x_intercept_marker.set_data([x_next], [0])
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

ax.set_title("Newton-Raphson Visualization with Tangents and Projections")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)


plt.show()
