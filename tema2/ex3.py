import numpy as np
import matplotlib.pyplot as plt
import sounddevice
import scipy

def a(t):
    return np.sin(2 * np.pi * 400 * t)

def b(t):
    return np.sin(2 * np.pi * 800 * t)

def c(t):
    return np.mod(t, 1/240)

def d(t):
    return np.sin(2 * np.pi * 300 * t)

x1 = np.linspace(0, 5, 40000)

sounddevice.play(a(x1), 44100)
sounddevice.wait()
sounddevice.play(b(x1), 44100)
sounddevice.wait()
sounddevice.play(c(x1), 44100)
sounddevice.wait()




rate = int(10e5)
scipy.io.wavfile.write('a.wav', rate, np.sign(d(x1)))

rate, x = scipy.io.wavfile.read('a.wav')

sounddevice.play(x, 44100)
sounddevice.wait()