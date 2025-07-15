#!/usr/bin/env python3
"""
oscillator_stream.py
SKA Harmonic Oscillator Stream Generator
Based on Cieśliński & Ratkiewicz (2005): arXiv:physics/0507182

Provides real-time position data stream for SKA learning process
Using exact discretization: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0
"""

import numpy as np
import time
from typing import Generator, Tuple


class HarmonicOscillatorStream:
    """
    Generate exact harmonic oscillator position stream for SKA learning
    
    Usage:
        stream = HarmonicOscillatorStream(omega=1.0, epsilon=0.01, phi=0.0)
        for position in stream.get_positions(num_steps=1000):
            # Feed position to SKA learning algorithm
            ska_learner.process(position)
    """
    
    def __init__(self, omega: float = 1.0, epsilon: float = 0.01, 
                 x0: float = 1.0, v0: float = 0.0, phi: float = 0.0):
        """
        Initialize harmonic oscillator stream
        
        Args:
            omega: Angular frequency ω (rad/s), must be non-zero
            epsilon: Time step ε (s), must be positive
            x0: Initial position
            v0: Initial velocity
            phi: Phase φ (radians)  # NEW: Added phase parameter
        """
        # Validate inputs
        if omega == 0:
            raise ValueError("Angular frequency omega cannot be zero.")
        if epsilon <= 0:
            raise ValueError("Time step epsilon must be positive.")
        
        self.omega = omega
        self.epsilon = epsilon
        self.x0 = x0
        self.v0 = v0
        self.phi = phi  # NEW: Store phase
        
        # Initialize state using analytical solution with phase
        self.x_prev = x0 * np.cos(phi) + (v0 / omega) * np.sin(phi)  # x_{n-1} at t=0
        self.x_curr = x0 * np.cos(omega * epsilon + phi) + (v0 / omega) * np.sin(omega * epsilon + phi)  # x_n at t=ε
        self.step_count = 1
        
    def reset(self):
        """Reset oscillator to initial conditions"""
        self.x_prev = self.x0 * np.cos(self.phi) + (self.v0 / self.omega) * np.sin(self.phi)
        self.x_curr = self.x0 * np.cos(self.omega * self.epsilon + self.phi) + (self.v0 / self.omega) * np.sin(self.omega * self.epsilon + self.phi)
        self.step_count = 1
    
    def next_position(self) -> float:
        """
        Compute next position using exact discretization
        
        Returns:
            float: Next position x_{n+1}
        """
        # Exact discretization formula: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0
        x_next = 2 * np.cos(self.omega * self.epsilon) * self.x_curr - self.x_prev
        
        # Update state for next iteration
        self.x_prev = self.x_curr
        self.x_curr = x_next
        self.step_count += 1
        
        return x_next
    
    def get_positions(self, num_steps: int) -> Generator[float, None, None]:
        """
        Generate stream of positions for SKA learning
        
        Args:
            num_steps: Number of position values to generate
            
        Yields:
            float: Position values x_n
        """
        for _ in range(num_steps):
            yield self.next_position()
    
    def get_positions_with_time(self, num_steps: int) -> Generator[Tuple[float, float], None, None]:
        """
        Generate stream of (time, position) pairs
        
        Args:
            num_steps: Number of data points to generate
            
        Yields:
            Tuple[float, float]: (t_n, x_n) pairs
        """
        for step in range(num_steps):
            t_n = step * self.epsilon
            x_n = self.next_position()
            yield t_n, x_n
    
    def get_infinite_stream(self) -> Generator[float, None, None]:
        """
        Generate infinite stream of positions
        
        Yields:
            float: Position values x_n (infinite)
        """
        while True:
            yield self.next_position()
    
    def get_real_time_stream(self, duration: float = None) -> Generator[float, None, None]:
        """
        Generate real-time position stream (with actual time delays)
        
        Args:
            duration: Run for this many seconds (None = infinite)
            
        Yields:
            float: Position values x_n with real-time delays
        """
        start_time = time.time()
        
        while True:
            if duration is not None and (time.time() - start_time) >= duration:
                break
                
            position = self.next_position()
            yield position
            time.sleep(self.epsilon)  # Real-time simulation
    
    def get_batch(self, num_steps: int) -> np.ndarray:
        """
        Generate batch of positions as numpy array
        
        Args:
            num_steps: Number of positions to generate
            
        Returns:
            np.ndarray: Array of position values
        """
        return np.array([self.next_position() for _ in range(num_steps)])
    
    @property
    def current_state(self) -> dict:
        """Get current oscillator state"""
        return {
            'x_prev': self.x_prev,
            'x_curr': self.x_curr,
            'step_count': self.step_count,
            'omega': self.omega,
            'epsilon': self.epsilon,
            'phi': self.phi  # NEW: Include phase in state
        }


def create_test_stream(omega: float = 1.0, epsilon: float = 0.01, 
                      x0: float = 1.0, v0: float = 0.0, phi: float = 0.0) -> np.ndarray:
    """
    Convenience function to create test data for SKA learning
    
    Args:
        omega: Angular frequency (rad/s)
        epsilon: Time step (s)
        x0: Initial position
        v0: Initial velocity
        phi: Phase (radians)  # NEW: Added phase parameter
        
    Returns:
        np.ndarray: Position values for SKA learning
    """
    stream = HarmonicOscillatorStream(omega=omega, epsilon=epsilon, x0=x0, v0=v0, phi=phi)
    return stream.get_batch(num_steps=1000)


def demo_ska_integration():
    """Demonstrate how to use with SKA learning process"""
    print("SKA Integration Demo")
    print("=" * 30)
    
    # Create oscillator stream with phase
    stream = HarmonicOscillatorStream(omega=2.0, epsilon=0.01, x0=1.0, v0=0.0, phi=np.pi/4)
    
    print(f"Parameters: ω=2.0 rad/s, ε=0.01 s, x₀=1.0, v₀=0.0, φ={np.pi/4:.3f} rad")
    print("Generating position stream for SKA learning...")
    print("Position values (first 20):")
    
    # Example: Feed positions to SKA learner
    for i, position in enumerate(stream.get_positions(20)):
        print(f"Step {i:2d}: x_n = {position:8.6f}")
        
        # Here you would feed position to your SKA learner:
        # ska_learner.process(position)
    
    print("\nBatch generation example:")
    stream.reset()  # Reset to initial conditions
    batch = stream.get_batch(100)
    print(f"Generated batch shape: {batch.shape}")
    print(f"Batch stats: min={batch.min():.6f}, max={batch.max():.6f}, std={batch.std():.6f}")


def continuous_stream():
    """Run continuous data stream for SKA learning"""
    print("SKA Harmonic Oscillator - Continuous Data Stream")
    print("Exact discretization: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0")
    print("=" * 60)
    
    # Parameters
    omega = 1.0      # Angular frequency (rad/s)
    epsilon = 0.01   # Time step (s)
    x0 = 1.0         # Initial position
    v0 = 0.0         # Initial velocity
    phi = np.pi/4    # Phase (radians)  # NEW: Added phase parameter
    
    print(f"ω = {omega} rad/s")
    print(f"ε = {epsilon} s")
    print(f"Initial: x₀ = {x0}, v₀ = {v0}, φ = {phi:.3f} rad ({phi*180/np.pi:.1f}°)")
    print("\nStreaming positions (press Ctrl+C to stop)...")
    print("Format: step_n, position_x_n")
    print("-" * 40)
    
    # Create oscillator stream
    stream = HarmonicOscillatorStream(omega=omega, epsilon=epsilon, x0=x0, v0=v0, phi=phi)
    
    try:
        step = 0
        for position in stream.get_infinite_stream():  # Infinite stream
            print(f"{step:6d}, {position:12.8f}")
            step += 1
            
            # Optional: Add small delay for readability
            # time.sleep(0.001)  # Uncomment for slower output
            
    except KeyboardInterrupt:
        print(f"\nStream stopped at step {step}")
        print("Final state:", stream.current_state)


if __name__ == "__main__":
    # Run continuous stream by default
    continuous_stream()
    
    # Uncomment for demo instead:
    # demo_ska_integration()