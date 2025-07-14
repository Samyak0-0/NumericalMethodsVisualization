#Given data
x_values = [0, 1, 3, 4, 5]
y_values = [0, 1, 81, 256, 625]

x_to_estimate = 2

def LagrangeConstant(x_to_est, i):
    
    lagrange_constant = 1
    for k in range(len(x_values)):
        if( k== i):
            continue;
        lagrange_constant *= (x_to_est-x_values[k]) / (x_values[i] - x_values[k])
    return lagrange_constant


def LagrangeInterpolation(x):
    
    EstimatedValue = 0
    for i in range(len(x_values)):
        EstimatedValue += LagrangeConstant(x, i) * y_values[i]

    return EstimatedValue


print(f"From Lagrange Interpolation, y({x_to_estimate}) = {LagrangeInterpolation(x_to_estimate)}")