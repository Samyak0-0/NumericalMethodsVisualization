import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def f(x):
    return x**2 - np.sin(x)


def bisection_method(f, a, b, tol=1e-4, max_iter=100):
    results = []
    print("-----------------------------------------------------------------------")
    print("iter        a              b              c              f(c)")
    print("-----------------------------------------------------------------------")
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        results.append((i, a, b, c, fc))
        print(f"  {i:<4d}    {a:<8.4f}       {b:<8.4f}       {c:<8.4f}       {fc:<.4f}")
        if abs(fc) < tol or (b - a) / 2 < tol:
            break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return results

results = bisection_method(f, a=0.5, b=1)
print(f"\nThe root of the equation f(X) = x^2 - sin(x) = 0 is {results[-1][3]:.4f}.")


# Plotting and Visualization
class StepPlot:
    def __init__(self, results, f):
        self.results = results
        self.f = f
        self.index = 0
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        self.plot_step()

        # Buttons
        axprev = plt.axes([0.6, 0.05, 0.1, 0.075])
        axnext = plt.axes([0.71, 0.05, 0.1, 0.075])
        self.bnext = Button(axnext, 'Next')
        self.bnext.on_clicked(self.next_step)
        self.bprev = Button(axprev, 'Previous')
        self.bprev.on_clicked(self.prev_step)

        plt.show()

    def plot_step(self):
        self.ax.clear()
        x = np.linspace(0, 1.2, 400)
        y = self.f(x)
        self.ax.plot(x, y, label='f(x) = x² - sin(x)')
        self.ax.axhline(0, color='black', linewidth=0.5)

        i, a, b, c, fc = self.results[self.index]
        self.ax.axvline(a, color='red', linestyle='--', label='a')
        self.ax.axvline(b, color='blue', linestyle='--', label='b')
        self.ax.axvline(c, color='green', linestyle='--', label='c')                

        self.ax.set_title(f'Iteration {i}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {fc:.4f}')
        self.ax.legend()
        self.fig.canvas.draw()

    def next_step(self, event):
        if self.index < len(self.results) - 1:
            self.index += 1
            self.plot_step()

    def prev_step(self, event):
        if self.index > 0:
            self.index -= 1
            self.plot_step()


StepPlot(results, f)