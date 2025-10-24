import numpy as np
import matplotlib.pyplot as plt

x0 = np.arange(0, 0.03, 0.0001)

def x(t):
    return np.cos(520 * np.pi * t + np.pi / 3)

def y(t):
    return np.cos(280 * np.pi * t - np.pi / 3)

def z(t):
    return np.cos(120 * np.pi * t + np.pi / 3)



fig, axs = plt.subplots(3)

axs[0].plot(x0, x(x0))
axs[1].plot(x0, y(x0))
axs[2].plot(x0, z(x0))

plt.show()
