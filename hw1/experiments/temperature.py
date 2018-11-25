import numpy as np
# this import is OK according to staff
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

X = np.array([400, 450, 900, 390, 550])
X.sort()
a = min(X)
N = 5
T = np.linspace(start=0.01, stop=5, num=100)

def pr(x_i):
    n_smallest = X[:N]
    return ((x_i/a)**(-1/T)) / sum([(s/a)**(-1/T) for s in n_smallest])


# P[i] is the curve pr(x_i) as function of T
P = np.array([pr(x_i) for x_i in X])
P = P.transpose()

print(P)

for i in range(len(X)):
    plt.plot(T, P[:, i], label=str(X[i]))

plt.xlabel("T")
plt.ylabel("P")
plt.title("Probability as a function of the temperature")
plt.legend()
plt.grid()
plt.show()
exit()
