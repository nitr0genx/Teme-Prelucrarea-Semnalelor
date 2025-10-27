import numpy as np
import matplotlib.pyplot as plt
import sounddevice

def a(t):
    return np.sin(2 * np.pi * 400 * t)

def b(t):
    return np.sin(2 * np.pi * 800 * t)


x1 = np.linspace(0, 5, 40000)

signal = np.concatenate((a(x1), b(x1)))

sounddevice.play(signal, 44100)
sounddevice.wait()