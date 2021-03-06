import numpy as np 

def numerical_diff(f,x):
    h = 1e-4
    return (f(x+h)-f(x-h)) / (2*h)

def function_1(x):
    return 0.01*x**2 + 0.1*x

def function_2(x):
    return np.sum(x**2)

def function_temp1(x0):
    return x0*x0 + 4.0**2.0

print(numerical_diff(function_1, 5)) # 0.1999999999990898
print(numerical_diff(function_temp1, 3.0)) # 6.00000000000378

