import numpy as np
import matplotlib.pyplot as plt

n = 8
mat = np.zeros((n, n), dtype=complex)

for i in range(n):
    for j in range(n):
        mat[i, j] = np.cos(2 * np.pi * i * j / n) - 1j * np.sin(2 * np.pi * i * j / n)



fig, axs = plt.subplots(2)

# Se ruleaza cate 2 in acelasi timp ca sa se vada mai bine pe ecran

axs[0].scatter(mat[0].real, mat[0].imag)
axs[1].scatter(mat[1].real, mat[1].imag)

# axs[0].scatter(mat[2].real, mat[2].imag)
# axs[1].scatter(mat[3].real, mat[3].imag)

# axs[0].scatter(mat[4].real, np.round(mat[4].imag, 15)) # daca nu pun round aici da ceva ciudat, partea imaginara se duce la 5 O_o
# axs[1].scatter(mat[5].real, mat[5].imag)

# axs[0].scatter(mat[6].real, mat[6].imag)
# axs[1].scatter(mat[7].real, mat[7].imag)

plt.show()

mat_H = mat.conj().T

prod = mat_H @ mat

print(np.allclose(prod, n * np.eye(n)))
