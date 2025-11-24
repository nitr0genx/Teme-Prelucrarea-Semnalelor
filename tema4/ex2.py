import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.sin(2 * np.pi * 70 * t)

def y(t):
    return np.sin(2 * np.pi * 170 * t)

def z(t):
    return np.sin(2 * np.pi * 270 * t)


a = np.linspace(0, 1, 100, endpoint=False)
b = a[:7]
c = np.linspace(0, 0.061, 500)

fig, axs = plt.subplots(3)

axs[0].stem(b, x(b))
axs[0].plot(c, x(c))

axs[1].stem(b, x(b))
axs[1].plot(c, y(c))

axs[2].stem(b, x(b))
axs[2].plot(c, z(c))
plt.show()