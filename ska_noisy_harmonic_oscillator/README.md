# SKA Noise Sensitivity – Harmonic Oscillator Benchmark

## Overview

This folder presents a systematic study of **SKA (Structured Knowledge Accumulation) real-time learning applied to a simple harmonic oscillator** with increasing levels of Gaussian noise.
The results demonstrate SKA’s extraordinary sensitivity to noise and its value as a universal calibrator for information geometry and regime detection.



## Folder Structure

```
ska_noise_harmonic_oscillator/
├── without_noise.png
├── noise_0.0001.png
├── noise_0.001.png
├── noise_0.01.png
└── README.md
```


## 1. Noise-Free Oscillator (Baseline Reference)

![Without Noise](without_noise.png)

* **All SKA variables are smooth, periodic, and symmetric.**
* **Entropy, knowledge, and decision** precisely follow the physical trajectory.
* **Lagrangian phase portrait**: a perfect, closed, symmetric curve.
* **Interpretation:** This is the gold standard for maximal order and predictability—**the universal “information geometry calibrator.”**



## 2. Noise Amplitude: 0.0001 (Threshold of Sensitivity)

![Noise 0.0001](noise_0.0001.png)

* **SKA variables remain nearly identical to the noise-free case**, with only minute deviations.
* The information geometry is still highly regular and ordered.
* **Interpretation:** SKA treats signals with noise ≤ 0.0001 as effectively deterministic—**this is the lower sensitivity bound**.



## 3. Noise Amplitude: 0.001 (Onset of Disorder)

![Noise 0.001](noise_0.001.png)

* **Mild irregularities appear in entropy and knowledge;** occasional bursts and “incipient crises.”
* The Lagrangian phase portrait develops fine structure but is not yet fully chaotic.
* **Interpretation:** This is the *intermediate regime*: SKA begins to detect unpredictability, mapping the earliest loss of information order.



## 4. Noise Amplitude: 0.01 (Full Breakdown)

![Noise 0.01](noise_0.01.png)

* **SKA variables become highly irregular and bursty;** entropy spikes, decision locks, and large fluctuations dominate.
* **Lagrangian phase portrait**: closed symmetry is lost; a complex, scattered “cloud” forms.
* **Interpretation:** **A 100x increase in noise amplitude transforms the system from order to chaos**—demonstrating SKA’s ultra-high sensitivity and its utility for detecting phase transitions.



## Scientific Insights

* **SKA acts as a real-time microscope for predictability,** detecting noise levels down to $10^{-4}$.
* The transition from order to disorder is **abrupt and visually dramatic**—SKA variables serve as a universal benchmark for information structure in any time series.
* **This calibration ladder provides a reference standard** for analyzing regime transitions in physical, biological, financial, and engineering data.



## How to Use These Results

* **Compare real-world SKA outputs to this set of calibrator plots** to objectively classify their predictability and noise sensitivity.
* **Signals that match the “without noise” or “0.0001” plots are maximally predictable.**
* **Signals resembling the “0.01” plot are chaotic or regime-shifting.**
* The intermediate “0.001” case helps identify *incipient disorder*—critical for early warning in complex systems.



## Citation

If you use these results or plots, please cite:

```
Bouarfa Mahi, "SKA Noise Sensitivity: Harmonic Oscillator Calibration" (2025).
https://github.com/quantiota/SKA-noise-harmonic-oscillator
```


