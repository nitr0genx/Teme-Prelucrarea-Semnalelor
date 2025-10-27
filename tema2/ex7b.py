import numpy as np
import matplotlib.pyplot as plt

def a(t):
    return np.sin(2 * np.pi * 60 * t)

x0 = np.linspace(0, 1, 1000)
x1 = x0[1::4]

fig, axs = plt.subplots(2)

axs[0].plot(x0, a(x0))
axs[1].plot(x1, a(x1)) # arata ca la punctul a dar putin shiftat

plt.show()