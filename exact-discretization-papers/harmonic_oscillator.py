#!/usr/bin/env python3
"""
SKA Harmonic Oscillator Data Generator
Based on Cieśliński & Ratkiewicz (2005): arXiv:physics/0507182

Generates real-time data stream: timestamp, position, frequency
Using exact discretization: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0
"""

import numpy as np
import time
import json
import matplotlib.pyplot as plt


class SKAHarmonicOscillator:
    """Generate real-time harmonic oscillator data for SKA framework"""
    
    def __init__(self, omega=1.0, epsilon=0.01, x0=1.0, v0=0.0):
        """
        Args:
            omega: Angular frequency ω
            epsilon: Time step ε  
            x0: Initial position
            v0: Initial velocity
        """
        self.omega = omega
        self.epsilon = epsilon
        
        # Initialize using analytical solution
        self.x_prev = x0  # x_{n-1}
        self.x_curr = x0 * np.cos(omega * epsilon) + (v0 / omega) * np.sin(omega * epsilon)  # x_n
        
        self.step_count = 1
        self.start_time = time.time()
    
    def step(self):
        """
        One step of exact discretization
        Returns: (timestamp, position, frequency)
        """
        # Exact discretization formula: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0
        x_next = 2 * np.cos(self.omega * self.epsilon) * self.x_curr - self.x_prev
        
        # Update for next iteration
        self.x_prev = self.x_curr
        self.x_curr = x_next
        self.step_count += 1
        
        # Generate output data
        timestamp = time.time()
        amplitude = x_next  # Position x_n (oscillates +/-)
        frequency = self.omega
        
        return timestamp, amplitude, frequency
    
    def generate_stream(self, duration=None, num_steps=None):
        """
        Generate data stream
        Args:
            duration: Run for this many seconds (OR)
            num_steps: Generate this many data points
        """
        if duration is not None:
            end_time = time.time() + duration
            while time.time() < end_time:
                yield self.step()
                time.sleep(self.epsilon)  # Real-time simulation
        
        elif num_steps is not None:
            for _ in range(num_steps):
                yield self.step()
        
        else:
            # Infinite stream
            while True:
                yield self.step()


def main():
    """Generate SKA test data"""
    print("SKA Harmonic Oscillator Data Generator")
    print("Exact discretization: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0")
    print("=" * 50)
    
    # Parameters
    omega = 1.0      # Angular frequency (rad/s)
    epsilon = 0.01   # Time step (s)
    x0 = 1.0         # Initial position
    v0 = 0.0         # Initial velocity
    
    print(f"ω = {omega} rad/s")
    print(f"ε = {epsilon} s")
    print(f"Initial: x₀ = {x0}, v₀ = {v0}")
    
    # Create oscillator
    oscillator = SKAHarmonicOscillator(omega, epsilon, x0, v0)
    
    # Generate data
    print(f"\nGenerating data stream...")
    print("Format: timestamp, position, frequency")
    print("-" * 40)
    
    data_points = []
    
    # Generate 1000 data points
    for i, (timestamp, amplitude, frequency) in enumerate(oscillator.generate_stream(num_steps=1000)):
        print(f"{timestamp:.6f}, {amplitude:.6f}, {frequency:.3f}")
        
        data_points.append({
            "step": i,
            "timestamp": timestamp,
            "position": amplitude,  # x_n (oscillating position)
            "frequency": frequency
        })
        
        # Show progress
        if (i + 1) % 100 == 0:
            print(f"--- Generated {i + 1} points ---")
    
    # Export to JSON for SKA framework
    output_data = {
        "metadata": {
            "omega": omega,
            "epsilon": epsilon,
            "initial_position": x0,
            "initial_velocity": v0,
            "total_points": len(data_points),
            "discretization": "exact_ciesliński"
        },
        "data": data_points
    }
    
    filename = f"ska_harmonic_data_{int(time.time())}.json"
    with open(filename, 'w') as f:
        json.dump(output_data, f, indent=2)
    
    print(f"\nData exported to: {filename}")
    
    # Plot the data
    timestamps = [point["timestamp"] for point in data_points]
    positions = [point["position"] for point in data_points]
    
    # Convert timestamps to relative time (seconds from start)
    start_timestamp = timestamps[0]
    relative_times = [(ts - start_timestamp) for ts in timestamps]
    
    # Create discrete time steps
    discrete_times = [i * epsilon for i in range(len(positions))]
    
    plt.figure(figsize=(12, 6))

    # Plot discrete points (computed)
    plt.plot(
        discrete_times,
        positions,
        'o',
        color='dodgerblue',
        markersize=2,
        label=fr'$x_n$ (discrete, $\epsilon={epsilon}$ s)'
    )

    # Plot analytical solution
    t_analytical = np.linspace(0, max(discrete_times), 1000)
    x_analytical = x0 * np.cos(omega * t_analytical) + (v0 / omega) * np.sin(omega * t_analytical)
    plt.plot(
        t_analytical,
        x_analytical,
        '--',
        color='crimson',
        linewidth=2,
        alpha=0.8,
        label=r'$x(t) = x_0 \cos(\omega t) + \frac{v_0}{\omega} \sin(\omega t)$'
    )

    # Labels and legend
    plt.xlabel(r'Time $t_n = n\epsilon$ (s)', fontsize=12)
    plt.ylabel(r'Position $x_n$', fontsize=12)
    plt.title(r'Exact Discretization: $x_{n+1} - 2\cos(\omega \epsilon)x_n + x_{n-1} = 0$', fontsize=14)
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    plt.legend(fontsize=10, loc='upper right')

    # Info box

    # Main legend for curves (no box)
    # Main legend for curve labels (unboxed)
    plt.legend(fontsize=10, loc='upper right', frameon=False)

    # Boxed legend for initial conditions only
    initial_conditions = (
        "Initial Conditions\n"
        rf"$\omega = {omega}$ rad/s" + "\n"
        rf"$x_0 = {x0}$" + "\n"
        rf"$v_0 = {v0}$"
    )
    plt.gca().text(
        0.2, 0.98,
        initial_conditions,
        transform=plt.gca().transAxes,
        fontsize=10,
        verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.85),
        usetex=False  # Change to True if full LaTeX rendering is configured
    )



    plt.tight_layout()
    plt.savefig('harmonic_oscillator.png', dpi=300)  # High-quality output
    plt.show()

    
    print("Ready for SKA framework!")


def real_time_demo():
    """Real-time streaming demo"""
    print("Real-time SKA data stream (press Ctrl+C to stop)")
    
    oscillator = SKAHarmonicOscillator(omega=2.0, epsilon=0.05)
    
    try:
        for timestamp, amplitude, frequency in oscillator.generate_stream():
            print(f"{timestamp:.6f}, {amplitude:.6f}, {frequency:.3f}")
    except KeyboardInterrupt:
        print("\nStream stopped.")


if __name__ == "__main__":
    main()
    
    # Uncomment for real-time demo:
    # real_time_demo()
  
   