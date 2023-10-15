import numpy as np

def simulate_random_variable(f):
    Y = 0
    while Y == 0:
        X = np.random.choice(np.arange(1, 10))
        Y = np.random.binomial(n=1, p=f(X)/np.log10(2))
    return X

def f(x):
    return x

result = simulate_random_variable(f)
print("模拟的随机变量X:", result)
