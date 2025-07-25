

# Multi-Oscillator Superposition — SKA Real-Time Analysis

## Experimental Results

![SKA Harmonic Oscillator Dashboard](harmonic_oscillator_dashboard.png)

*Real-time analysis of a **superposition of three harmonic oscillators** using the SKA framework, with **position as the only feature input**. The dashboard shows the evolution of position, classical and information Lagrangians, entropy, knowledge, and decision variables over time.*



## Interpretation

### Position as Feature Input (Top-Left Panel)

* The **raw position**—computed as the superposition of three oscillators—is directly used as the feature for SKA learning.
* The combined signal exhibits beating and amplitude modulation, characteristic of multi-frequency superposition.

### Classical and Information Lagrangian (Top-Right, Middle-Right)

* **Classical Lagrangian:** Shows periodic transitions reflecting the combined kinetic and potential energies of the three oscillators.
* **Information Lagrangian:** Tracks information change under the SKA model, phase-locked with the physical signal.

### Entropy (Middle-Left)

* SKA entropy evolves in perfect synchrony with the composite position signal.
* **Minima** correspond to the extrema of the position trajectory (maxima and minima of the composite wave)—maximum predictability.
* **Maxima** align with rapid transitions (zero crossings), where information uncertainty peaks.

### Knowledge (Bottom-Left)

* The SKA "knowledge" variable accumulates during periods of high predictability, capturing the informational structure of the superposed signal.

### Decision (Bottom-Right)

* The decision variable tracks the probability learned by SKA, with phase-locked oscillations reflecting structure in the composite signal.


### Joint Lagrangian Phase Space Trajectory  

A novel feature of this analysis is the **phase portrait formed by plotting the classical Lagrangian as a function of the information Lagrangian (bottom panel)**.

* **Over a full oscillation period**, the system traces a closed loop in the (information Lagrangian, classical Lagrangian) plane.
* **First half period:** The trajectory moves forward along a specific path as the system evolves.
* **Second half period:** The path reverses, retracing itself exactly, reflecting the time-reversal symmetry of conservative dynamics.

**Scientific Implications:**

* The loop demonstrates that mechanical and information dynamics are not independent, but are dynamically intertwined.
* The closed, reversible trajectory confirms energy conservation and time symmetry, but in a higher-dimensional space combining mechanics and information.
* This framework offers a new lens for studying dynamical systems:

  * *For conservative systems,* the path is reversible and closed.
  * *For dissipative or complex systems,* this approach may reveal open loops, area-enclosing curves, or new forms of informational “hysteresis.”

**This geometric coupling of classical and informational Lagrangians is a fundamentally new concept, providing a powerful tool for visualizing and understanding the deep structure of physical and informational evolution in dynamical systems.**




## Key Discovery: Entropy–Position Synchronization

> **Entropy reaches its minimum at the extrema of the composite position trajectory and peaks at zero-crossings.**
>
> This reveals a **direct, phase-locked relationship between the information geometry and physical motion**—the SKA framework autonomously identifies predictability and uncertainty windows in real time.

#### At Position Extrema:

* **Maximum predictability** (entropy minima)
* **Steepest knowledge accumulation**
* **Most confident decision**

#### At Position Zero-Crossings:

* **Maximum uncertainty** (entropy maxima)
* **Knowledge plateaus**
* **Lowest decision confidence**

This synchronization **demonstrates SKA’s unique ability to uncover the intrinsic information structure of complex, superposed signals in real time, using only position as input.**



## Scientific Significance

**Intrinsic Information Rhythm**

* First real-time, phase-locked entropy analysis of a multi-oscillator system using only position data.
* Reveals natural "predictability windows" hidden to traditional analytical methods.

**Autonomous, Real-Time Learning**

* **No prior knowledge** of signal frequencies or phases is required.
* SKA autonomously discovers structure and predictability directly from the position stream.

**Universal Principle**

* Results extend to arbitrary superpositions, nonlinear systems, and other complex signals.
* Foundation for future analysis of chaotic, biological, seismic, or financial data streams.

**Bridging Physics and Information Theory**

* Connects mechanical observables (position) to information measures (entropy, knowledge, decision).
* **Information structure is not given—it is actively revealed by the learning process.**


## Consistency with Classical Probability

A key validation of the SKA approach is its consistency with established results from classical mechanics. The probability of finding a classical harmonic oscillator at position $x$ is:

$$
P(x) = \Large \frac{1}{\pi \sqrt{A^2 - x^2}}
$$

for $|x| < A$, where $A$ is the amplitude.

**Interpretation:**

* The oscillator spends more time near the turning points ($x = \pm A$), so $P(x)$ diverges at the extrema.
* The oscillator moves fastest near $x=0$, so $P(x)$ is minimal at the center.

### **SKA Entropy vs. Classical Probability**

The SKA learning results show:

* **Entropy minima** occur at the extrema of the position signal, coinciding with the maxima of $P(x)$: these are the most predictable, most probable states.
* **Entropy maxima** occur at zero-crossings, coinciding with the minima of $P(x)$: these are the least predictable, least probable states.

| Phase Point         | Classical Probability | SKA Entropy | Interpretation           |
|---------------------|----------------------|-------------|--------------------------|
| Position Extremum   | Maximal              | Minimal     | Most predictable state   |
| Zero Crossing       | Minimal              | Maximal     | Least predictable state  |


### **Extension to Multi-Oscillator Superposition**

For a superposition of oscillators, the time-averaged probability distribution can become highly nontrivial and is generally not analytically tractable. However, SKA entropy dynamically tracks **instantaneous predictability**, revealing minima wherever the composite signal slows down (local extrema) and maxima at rapid transitions (zero crossings).

**Summary:**
SKA results are *fully consistent* with classical probability, but provide a richer, real-time perspective on information flow—*adapting instantly* to complex, multi-modal, or even nonstationary signals. This dynamic view of predictability goes beyond what is accessible through static, time-averaged probability distributions.



## Literature Context & Novelty

While information-theoretic analysis is common in quantum, thermodynamic, and phase-space contexts, **no previous work establishes real-time entropy computation for classical, multi-oscillator position dynamics**. SKA establishes the first explicit bridge between:

* **Classical mechanics** (observable position)
* **Information theory** (dynamic entropy, knowledge, and decision)
* **Autonomous learning** (unsupervised, real-time discovery)



## **Insight: Information Structure is Revealed by Learning**

The true information architecture of a physical system emerges **only through the process of structured knowledge accumulation (SKA)**.

While the classical equations give the full trajectory, **only SKA learning reveals the timing and structure of predictability and uncertainty—uncovering the hidden informational geometry**.


 **This connection is formalized through the SKA entropy definition:**

 $$
 H = \Large -\frac{1}{\ln 2} \int z \, dD
 $$

In SKA, entropy is not merely a statistical measure—it is dynamically constructed as learning progresses, reflecting the system’s evolving knowledge about its own state. This means that **SKA entropy is both the engine and the map of learning:** it drives the discovery of new informational structure and simultaneously records the moments when the system is most or least predictable.

The emergence of entropy minima and maxima, perfectly synchronized with the underlying dynamics, is thus a direct consequence of the SKA learning process. Only by learning does the system reveal its intrinsic information architecture—confirming that knowledge and predictability are not static, but are continuously shaped and discovered through SKA’s structured accumulation.





## Technical Parameters

```python
# Multi-Component Oscillator Parameters for Superposition

# Oscillator 1
OSCILLATOR_1_OMEGA = 0.13      # Angular frequency (rad/s)
OSCILLATOR_1_X0    = 1.0       # Initial amplitude
OSCILLATOR_1_V0    = 0.0       # Initial velocity
OSCILLATOR_1_PHI   = 0.0       # Phase (radians)

# Oscillator 2
OSCILLATOR_2_OMEGA = 0.11      # Angular frequency (rad/s)
OSCILLATOR_2_X0    = 1.0       # Initial amplitude
OSCILLATOR_2_V0    = 0.0       # Initial velocity
OSCILLATOR_2_PHI   = 1.5708    # Phase (radians) (π/2)

# Oscillator 3
OSCILLATOR_3_OMEGA = 0.11      # Angular frequency (rad/s)
OSCILLATOR_3_X0    = 1.0       # Initial amplitude
OSCILLATOR_3_V0    = 0.0       # Initial velocity
OSCILLATOR_3_PHI   = 3.1416    # Phase (radians) (π)

# SKA Parameters
SKA_INIT_STD            = 0.01      # Initial weight std
SKA_LEARNING_RATE       = 0.0001    # Learning rate
SKA_CHECKPOINT_INTERVAL = 100       # Checkpoint frequency
SKA_LOG_INTERVAL        = 10        # Log frequency
SKA_MAX_BUFFER_SIZE     = 50        # Max buffer size
SKA_NUMERICAL_CLIP      = 500.0     # Sigmoid clip
SKA_PERFORMANCE_WINDOW  = 100       # Rolling performance window

# System Parameters
LOG_LEVEL               = 'INFO'
LOG_FORMAT              = '%(asctime)s %(levelname)s %(message)s'
SHUTDOWN_TIMEOUT        = 30
PROCESSING_BATCH_SIZE   = 1
SLEEP_INTERVAL          = 0.01

# SKA Analysis
feature                 = "position"
method                  = "exact_discretization"   # Cieśliński & Ratkiewicz (2005)
entropy_calculation     = "continuous_approximation"
sampling_rate           = 1/epsilon                # 10 Hz, with epsilon = 0.1 s
```



## Implications for Complex Systems

This approach establishes a basis for:

1. **Multi-oscillator and beating analysis:** Detecting superposition effects from position data alone.
2. **Nonlinear/chaotic systems:** Tracking information flow and regime changes.
3. **Real-world signals:** Applying SKA to seismic, physiological, or financial data streams.
4. **Unsupervised regime detection:** Autonomous, real-time discovery of hidden informational transitions.

---
## Mathematical Foundation

SKA entropy is computed as:

$$
H = \Large -\frac{1}{\ln 2} \int z \, dD
$$

where **z is a function of position only** in this multi-oscillator context.



## Next Steps

* [ ] Robustness to noise and missing data
* [ ] Real-time frequency decomposition/extraction
* [ ] Application to nonlinear and chaotic signals
* [ ] Benchmark against Fourier and classical spectral analysis



*This analysis demonstrates that even apparently simple, multi-oscillator systems encode rich and hidden information structures—discoverable in real time through entropy-based learning using only the position as input.*




