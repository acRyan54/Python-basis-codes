import sympy as sp
import numpy as np
from matplotlib import pyplot as plt


t = np.linspace(0, 1, 100)
x = 3*t - 3*t**2
y = 2 - 3*t**2 + 2*t**3
plt.plot(x, y)

plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.axis([-1, 2, -1, 2])
# plt.savefig("1.png",dpi=600)

plt.show()