import math

# Given data
x = [0.20, 0.22, 0.24, 0.26, 0.28, 0.30]
y = [1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139]
n = len(x)

# Step size
h = x[1] - x[0]

# Forward difference table
diff_table = [y.copy()]
for level in range(1, n):
    current_diffs = [diff_table[level-1][i+1] - diff_table[level-1][i] for i in range(n - level)]
    diff_table.append(current_diffs)

# Newton's Forward Interpolation for f(0.21)
x0 = x[0]
p = (0.21 - x0) / h

forward_result = y[0]
p_term = 1
for i in range(1, n):
    p_term *= (p - (i - 1))
    forward_result += (p_term / math.factorial(i)) * diff_table[i][0]

print(f"Estimated f(0.21) using Newton's Forward Interpolation: {forward_result:.4f}")


# Backward difference table (same as forward, just from the end)
# Newton's Backward Interpolation for f(0.29)
xn = x[-1]
p_back = (0.29 - xn) / h

backward_result = y[-1]
p_term = 1
for i in range(1, n):
    p_term *= (p_back + (i - 1))
    backward_result += (p_term / math.factorial(i)) * diff_table[i][-1]

print(f"Estimated f(0.29) using Newton's Backward Interpolation: {backward_result:.4f}")
