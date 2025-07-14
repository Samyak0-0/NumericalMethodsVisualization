import math

# Given data
x_values = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30]
y_values = [1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139]
n = len(x_values)
h = x_values[1] - x_values[0]


# Generating Difference Table
diff_table = [y_values.copy()]

for order in range(1, n):
    current_diffs=[]
    for i in range(n - order):
        diff = diff_table[order-1][i+1] - diff_table[order-1][i]
        current_diffs.append(diff)
    diff_table.append(current_diffs)


def ForwardInterpolation(x):

    interpolatedValue = y_values[0]
    p = (x-x_values[0])/h
    p_term = 1;

    for i in range(1,n):
        p_term *= (p-(i-1))
        interpolatedValue += (p_term / math.factorial(i)) * diff_table[i][0]
    
    return interpolatedValue


def BackwardInterpolation(x):

    interpolatedValue = y_values[-1]
    p = (x-x_values[-1])/h
    p_term = 1;

    for i in range(1,n):
        p_term *= (p+(i-1))
        interpolatedValue += (p_term / math.factorial(i)) * diff_table[i][n-i-1]
    
    return interpolatedValue


print(f"Using Newton's Forward Interpolation   f(0.21): {ForwardInterpolation(0.21):.4f}")
print(f"Using Newton's Backward Interpolation  f(0.29): {BackwardInterpolation(0.29):.4f}")