import numpy as np
from matplotlib import pyplot as plt

X = np.array([400,900,390,1000,550])
T = np.linspace(0.01, 5., 100)
alpha = min(X)

for x in X:
    y_line = [((x/alpha)**(-1/t))/sum((X/alpha)**(-1/t)) for t in T]
    plt.plot(T, y_line, label=x)

plt.xlabel("T")
plt.legend()
plt.ylim((0,1))
plt.grid(linestyle='dotted')
plt.title("Probability as a function of the temperature")
plt.show()