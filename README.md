# Wireless Communication Projects

This repository contains two Python-based projects focused on wireless communication fundamentals:

1. **Wireless Channel Simulation** — simulates digital modulation over noisy and fading channels, then compares BER performance.
2. **Signal Spectrum Analysis** — generates modulated signals, adds noise, and visualizes spectral effects.

## Repository Structure

```text
.
├── README.md
├── Wireless Channel Simulation/
│   ├── channel_simulation.py
│   ├── requirements.txt
│   └── README.md
└── Signal Spectrum Analysis/
    ├── signal_spectrum_analysis.py
    ├── requirements.txt
    └── README.md
```

## Projects Overview

### 1) Wireless Channel Simulation

Simulates transmission performance under:
- **AWGN channel**
- **Rayleigh fading channel**

Supported modulation schemes:
- **BPSK**
- **QPSK**
- **16-QAM**

Typical output:
- BER vs SNR curves for each modulation/channel combination.

Run:
```bash
cd "Wireless Channel Simulation"
pip install -r requirements.txt
python channel_simulation.py
```

### 2) Signal Spectrum Analysis

Performs signal generation and spectral analysis for:
- **BPSK**
- **QPSK**

Processing pipeline:
- Generate baseband/modulated signals
- Add AWGN noise
- Compare frequency spectra before and after noise

Run:
```bash
cd "Signal Spectrum Analysis"
pip install -r requirements.txt
python signal_spectrum_analysis.py
```

## Requirements

- Python 3.8+
- Dependencies listed in each project’s `requirements.txt`

To install both projects’ dependencies:

```bash
pip install -r "Wireless Channel Simulation/requirements.txt"
pip install -r "Signal Spectrum Analysis/requirements.txt"
```

## Learning Goals

This repo is useful for understanding:
- Digital modulation basics
- BER behavior across channel conditions
- Effect of AWGN on time/frequency-domain signal characteristics

## Notes

- Each subproject has its own README with project-specific details.
- You can run projects independently.
