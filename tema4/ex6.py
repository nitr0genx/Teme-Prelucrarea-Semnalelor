import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


fs, signal = wavfile.read("audio.wav")
signal = signal.astype(float)

n = len(signal)
len_grup = n // 100

grupuri = []

for i in range(0, n-len_grup, len_grup//2):
    grupuri.append(np.abs(np.fft.fft(signal[i:i+len_grup])))


grupuri = np.array(grupuri)


plt.imshow(10*np.log10(grupuri.T), aspect='auto', origin='lower', cmap='inferno')
plt.show()