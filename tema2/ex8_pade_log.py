import numpy as np
import matplotlib.pyplot as plt

def pade_sin(a):
    return (a - (7 * a ** 3) / 60) / (1 + (a ** 2) / 20)

x0 = np.linspace(-np.pi / 2, np.pi / 2, 1000)

fig, axs = plt.subplots(2)

axs[0].set_yscale('log')
axs[1].set_yscale('log')

axs[0].plot(x0, x0)
axs[0].plot(x0, pade_sin(x0))

axs[1].plot(x0, np.abs(x0 - pade_sin(x0)))
axs[1].set_ylabel('Eroarea absoluta')

plt.show()