import numpy as np
# this import is OK according to staff
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

X = np.array([400, 450, 900, 390, 550])
a = min(X)
N = 5

# create the temperature scale
T = np.linspace(start=0.01, stop=5, num=100)

# normelize the temperature vector
normelized_X = X/a

# allocate the result matrix
P = np.zeros((len(T), len(X)))

# initialize the correct values
for i in range(len(T)):
    mone = normelized_X**(-1 / T[i])
    mehane = sum(mone)
    for j in range(len(X)):
        P[i][j] = mone[j]/mehane

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
