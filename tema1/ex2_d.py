import numpy as np
import matplotlib.pyplot as plt

def d(t):
    return np.sin(2 * np.pi * 300 * t)

x0 = np.linspace(0, 0.03, 1600)

plt.plot(x0, np.sign(d(x0)))
plt.show()
