# SKA Harmonic Oscillator


**Real-Time Entropy Learning on a Discrete Harmonic Oscillator using Structured Knowledge Accumulation (SKA)**

This repository applies the **Structured Knowledge Accumulation (SKA)** framework to the **discrete harmonic oscillator**, serving as a minimal testbed for real-time entropy learning in low-entropy, time-reversible systems.

By leveraging exact discretizations from classical mathematical physics, we evaluate SKA's behavior in periodic, deterministic environments and compare it to its performance in complex real-world signals (e.g., market, physiological or seismic data).



## What is SKA?

SKA is an unsupervised learning paradigm that models intelligence as **entropy-driven knowledge accumulation**. It replaces backpropagation with **forward-only learning** and tracks decision probabilities as a function of entropy gradients.

For this project:
- The SKA learner consumes oscillator states $x_n$ as a real-time stream
- It evolves its internal state using entropy minimization
- It outputs decision values, entropy trajectories, and phase signatures



##  Theoretical Foundation

This project builds on two key mathematical papers:

- **Cieśliński & Ratkiewicz (2005)** – [arXiv:physics/0507182](https://arxiv.org/abs/physics/0507182)  
  Introduces *exact discretizations* of the harmonic oscillator including:


  $$\large x_{n+2} - 2 \cos(\omega \epsilon) x_{n+1} + x_n = 0$$


- **Cieśliński (2009)** – [arXiv:0911.3672](https://arxiv.org/abs/0911.3672)  
  Extends to damped, driven, and multidimensional oscillators with energy-preserving and symplectic discretizations

These allow perfect simulation of the continuous oscillator in a discrete-time SKA learning loop.


##  Features

- ✅ Real-time streaming of discrete harmonic oscillator signals
- ✅ SKA learner integration with entropy and decision logging
- ✅ Visualizations of entropy trajectories and cosine alignment
- ✅ Comparison with theoretical analytic solutions
- ✅ Configurable oscillator type: undamped, damped, or driven



##  Quick Start

```bash
git clone https://github.com/yourname/SKA-Harmonic-Oscillator.git
cd SKA-Harmonic-Oscillator
pip install -r requirements.txt
python ska_oscillator.py
````



##  Structure

```text
ska_harmonic_oscillator/
│
├── ska_oscillator.py         # Main script: oscillator + SKA learner
├── oscillator_stream.py      # Generator for x_n using exact discretization
├── ska_entropy.py            # Entropy evolution and SKA core logic
├── plots/                    # Output visualizations
│   ├── entropy_vs_time.png
│   └── decision_cosine.png
├── requirements.txt
└── README.md
```



##  Research Goals

* Test SKA’s performance in a **fully deterministic** setting
* Analyze how entropy behaves under **cyclical, low-entropy** input
* Establish this setup as a **minimal benchmark** for SKA evolution
* Observe transitions in decision variables $\mathbb{D}_n$ over harmonic cycles
* Explore the impact of **controlled perturbations** (e.g., damping or noise)



##  Related Work

* [SKA-Quantitative-Finance](https://github.com/quantiota/SKA-quantitative-finance) – entropy learning on live market data
* [SKA-Heart-Rate-Variability](https://github.com/quantiota/SKA-Heart-Rate-Variability) – entropy detection in physiological time series
* [SKA-RealTime-Seismic](https://github.com/quantiota/SKA-RealTime-Seismic) – entropy detection in seismic time series


##  License

MIT


##  Citation

If this work inspires your research, please cite the following:

> Bouarfa Mahi. Structured Knowledge Accumulation: An Entropy-Based Framework for Real-Time Learning in Discrete Systems. *(working paper, 2025)*



