import numpy as np
import matplotlib.pyplot as plt

def a(t, phi):
    return np.sin(2 * np.pi * 3 * t + phi)

x0 = np.linspace(0, 1, 1000)

s1 = a(x0, 0)
s2 = a(x0, np.pi / 3)
s3 = a(x0, 2 * np.pi / 3)
s4 = a(x0, np.pi)

z = np.random.normal(loc=0, scale=1, size=1000)

g1 = np.sqrt(np.linalg.norm(s1) ** 2 / (0.1 * np.linalg.norm(z) ** 2))
g2 = np.sqrt(np.linalg.norm(s2) ** 2 / (1.0 * np.linalg.norm(z) ** 2))
g3 = np.sqrt(np.linalg.norm(s3) ** 2 / (10  * np.linalg.norm(z) ** 2))
g4 = np.sqrt(np.linalg.norm(s4) ** 2 / (100 * np.linalg.norm(z) ** 2))

plt.plot(x0, s1 + g1 * z)
plt.plot(x0, s2 + g2 * z)
plt.plot(x0, s3 + g3 * z)
plt.plot(x0, s4 + g4 * z)


plt.show()