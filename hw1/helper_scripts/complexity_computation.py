import numpy as np

l = 5

def no_gas(k):
    return np.math.factorial(k)

def with_gas(k):
    return no_gas(k) * (l**(k-1))


for k in range(1, 11):
    print("k: {}\t no_gas: {}\t with_gas: {}\r".format(k, no_gas(k), with_gas(k)))
