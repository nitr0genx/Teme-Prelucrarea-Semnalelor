import numpy as np
import matplotlib.pyplot as plt

def a(t):
    return np.sin(2 * np.pi * 400 * t)

def b(t):
    return np.sin(2 * np.pi * 800 * t)

def c(t):
    return np.mod(t, 1/240)

fig, axs = plt.subplots(3)

x0 = np.linspace(0, 0.03, 1600)
x1 = np.linspace(0, 3, 2000)
x2 = np.linspace(0, 0.03, 1600)

axs[0].plot(x0, a(x0))
axs[1].plot(x1, b(x1))
axs[2].plot(x2, c(x2))

plt.show()
