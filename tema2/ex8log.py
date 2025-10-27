import numpy as np
import matplotlib.pyplot as plt

x0 = np.linspace(-np.pi / 2, np.pi / 2, 1000)

fig, axs = plt.subplots(2)

axs[0].set_yscale('log')
axs[1].set_yscale('log')

axs[0].plot(x0, x0)
axs[0].plot(x0, np.sin(x0))

axs[1].plot(x0, np.abs(x0 - np.sin(x0)))
axs[1].set_ylabel('Eroarea absoluta')

plt.show()