import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.sin(2 * np.pi * 3 * t)

a = np.linspace(0, 1, 3000, dtype=complex)

def z(omega):
    res = x(a)

    for i in range(3000):
        res[i] = res[i] * (np.cos(2 * np.pi * omega * a[i]) - 1j * np.sin(2 * np.pi * omega * a[i]))

    return res


fig, axs = plt.subplots(3, 2)



for ax in axs.flat:
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.grid(True)

axs[0, 0].scatter(a, x(a), s=1, linewidth=0)
axs[0, 0].set_title('Semnal frecventa 3')

axs[0, 1].scatter(z(1).real, z(1).imag, c=np.sqrt(z(1).real ** 2 + z(1).imag ** 2), cmap='viridis', s=1, linewidth=0)
axs[0, 1].set_title('Frecventa 1')

axs[1, 0].scatter(z(3).real, z(3).imag, c=np.sqrt(z(3).real ** 2 + z(3).imag ** 2), cmap='viridis', s=1, linewidth=0)
axs[1, 0].set_title('Frecventa 3')

axs[1, 1].scatter(z(5).real, z(5).imag, c=np.sqrt(z(5).real ** 2 + z(5).imag ** 2), cmap='viridis', s=1, linewidth=0)
axs[1, 1].set_title('Frecventa 5')

axs[2, 0].scatter(z(8).real, z(8).imag, c=np.sqrt(z(8).real ** 2 + z(8).imag ** 2), cmap='viridis', s=1, linewidth=0)
axs[2, 0].set_title('Frecventa 8')

axs[2, 1].scatter(z(9).real, z(9).imag, c=np.sqrt(z(9).real ** 2 + z(9).imag ** 2), cmap='viridis', s=1, linewidth=0)
axs[2, 1].set_title('Frecventa 9')

plt.tight_layout()
plt.show()

