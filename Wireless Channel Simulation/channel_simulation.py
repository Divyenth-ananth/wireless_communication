
import numpy as np
import matplotlib.pyplot as plt

def awgn_channel(signal, snr_db):
    snr_linear = 10**(snr_db / 10)
    noise_power = np.mean(np.abs(signal)**2) / snr_linear
    noise = np.sqrt(noise_power/2) * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))
    return signal + noise

def rayleigh_channel(signal):
    fading = (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal))) / np.sqrt(2)
    return signal * fading

def ber_bpsk(snr_db, channel_type='AWGN'):
    bits = np.random.randint(0, 2, 10000)
    symbols = 2*bits - 1

    if channel_type == 'Rayleigh':
        symbols = rayleigh_channel(symbols)

    received = awgn_channel(symbols, snr_db)

    detected_bits = (received.real > 0).astype(int)
    ber = np.mean(detected_bits != bits)
    return ber

def ber_qpsk(snr_db, channel_type='AWGN'):
    bits = np.random.randint(0, 2, 20000)
    symbols = (2*bits[0::2]-1) + 1j*(2*bits[1::2]-1)

    if channel_type == 'Rayleigh':
        symbols = rayleigh_channel(symbols)

    received = awgn_channel(symbols, snr_db)

    detected_bits = np.zeros(2*len(symbols), dtype=int)
    detected_bits[0::2] = (received.real > 0).astype(int)
    detected_bits[1::2] = (received.imag > 0).astype(int)

    ber = np.mean(detected_bits != bits)
    return ber

def plot_ber_curves():
    snr_range = np.arange(0, 20, 2)
    ber_bpsk_awgn = [ber_bpsk(snr, 'AWGN') for snr in snr_range]
    ber_bpsk_rayleigh = [ber_bpsk(snr, 'Rayleigh') for snr in snr_range]
    ber_qpsk_awgn = [ber_qpsk(snr, 'AWGN') for snr in snr_range]
    ber_qpsk_rayleigh = [ber_qpsk(snr, 'Rayleigh') for snr in snr_range]

    plt.figure(figsize=(10, 6))
    plt.semilogy(snr_range, ber_bpsk_awgn, label='BPSK - AWGN', marker='o')
    plt.semilogy(snr_range, ber_bpsk_rayleigh, label='BPSK - Rayleigh', marker='o')
    plt.semilogy(snr_range, ber_qpsk_awgn, label='QPSK - AWGN', marker='s')
    plt.semilogy(snr_range, ber_qpsk_rayleigh, label='QPSK - Rayleigh', marker='s')

    plt.xlabel('SNR (dB)')
    plt.ylabel('Bit Error Rate (BER)')
    plt.title('BER vs SNR for BPSK and QPSK')
    plt.legend()
    plt.grid(True, which='both')
    plt.savefig('plots/ber_vs_snr.png')
    plt.show()

if __name__ == '__main__':
    plot_ber_curves()
