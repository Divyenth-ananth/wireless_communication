import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def generate_bpsk_signal(bits, fs):
    symbols = 2 * bits - 1
    t = np.arange(0, len(symbols), 1) / fs
    signal = symbols
    return t, signal

def generate_qpsk_signal(bits, fs):
    symbols = (2*bits[0::2]-1) + 1j*(2*bits[1::2]-1)
    t = np.arange(0, len(symbols), 1) / fs
    return t, symbols

def add_awgn(signal, snr_db):
    snr_linear = 10**(snr_db / 10)
    power_signal = np.mean(np.abs(signal)**2)
    noise_power = power_signal / snr_linear
    noise = np.sqrt(noise_power/2) * (np.random.randn(len(signal)) + 1j*np.random.randn(len(signal)))
    return signal + noise

def plot_spectrum(signal, fs, title):
    N = len(signal)
    spectrum = fft(signal)
    freqs = fftfreq(N, 1/fs)
    plt.plot(freqs[:N//2], np.abs(spectrum[:N//2]))
    plt.title(title)
    plt.grid(True)

fs = 1000
bits = np.random.randint(0, 2, 1000)

t, bpsk_signal = generate_bpsk_signal(bits, fs)
bpsk_signal_noisy = add_awgn(bpsk_signal, 10)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plot_spectrum(bpsk_signal, fs, 'BPSK Spectrum (Clean)')
plt.subplot(1, 2, 2)
plot_spectrum(bpsk_signal_noisy, fs, 'BPSK Spectrum (Noisy)')
plt.savefig('plots/spectrum.png')
plt.show()
