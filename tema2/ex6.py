import numpy as np
import matplotlib.pyplot as plt

def a(t):
    return np.sin(2 * np.pi * 32 * t) # nici macar nu arata ca un sinus, arata haotic

def b(t):
    return np.sin(2 * np.pi * 16 * t) # arata ca un semnal triangle in loc de sinus

def c(t):
    return t*0

x0 = np.linspace(0, 1, 64, endpoint=False)

fig, axs = plt.subplots(3)

axs[0].plot(x0, a(x0))
axs[1].plot(x0, b(x0))
axs[2].plot(x0, c(x0))

plt.show()