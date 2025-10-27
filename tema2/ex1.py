import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.sin(2 * np.pi * t)

def g(t):
    return np.cos(2 * np.pi * t - np.pi / 2)

fig, axs = plt.subplots(2)

x0 = np.linspace(0, 1, 1600)

axs[0].plot(x0, f(x0))
axs[1].plot(x0, g(x0))

plt.show()
