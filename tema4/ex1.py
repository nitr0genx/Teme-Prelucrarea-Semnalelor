import numpy as np
import matplotlib.pyplot as plt
import time

def DFT(P):
    n = len(P)
    mat = np.zeros((n, n), dtype=complex)

    for i in range(n):
        for j in range(n):
            mat[i, j] = np.cos(2 * np.pi * i * j / n) - 1j * np.sin(2 * np.pi * i * j / n)

    return mat @ P

def FFT(P):
    n = len(P)

    if n == 1:
        return P
    
    x = np.exp(2 * np.pi * 1j / n)

    P_par = P[0::2]
    P_impar = P[1::2]
    y_par = FFT(P_par)
    y_impar = FFT(P_impar)
    
    y = np.zeros(n, dtype=complex)

    for i in range(n//2):
        y[i] = y_par[i] + x ** i * y_impar[i]
        y[i + n//2] = y_par[i] - x ** i * y_impar[i]

    return y

N = 8192

v = np.random.randint(low=1, high=100, size=N)

p1 = time.time()

print(DFT(v))
print()
p2 = time.time()

print(FFT(v))
print()
p3 = time.time()

print(np.fft.fft(v))
print()
p4 = time.time()


plt.plot(['DFT', 'FFT', 'np.fft.fft'], [p2-p1, p3-p2, p4-p3])
plt.yscale('log')
plt.ylabel('N = ' + str(N))
plt.show()
