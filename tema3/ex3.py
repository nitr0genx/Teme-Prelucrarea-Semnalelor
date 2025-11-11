import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return  4 * np.sin(2 * np.pi * 5 * t) +\
            2 * np.sin(2 * np.pi * 24 * t) +\
            np.sin(2 * np.pi * 57 * t)


a = np.linspace(0, 1, 2000)

x_val = x(a)

def f(omega):
    res = 0

    for i in range(2000):
        res += x_val[i] * np.exp(-2j * np.pi * i * omega / 2000)

    return res


vec = []

for i in range(1, 100):
    vec.append(np.abs(f(i)))

fig, axs = plt.subplots(2)

axs[0].plot(a, x_val)
axs[1].stem(range(1, 100), vec)

plt.show()