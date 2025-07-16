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
        for timestamp, position in stream.get_positions_with_timestamps(num_steps=1000):
            # Feed position to SKA learning algorithm
            ska_learner.process(timestamp, position)
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
            phi: Phase φ (radians)
        """
        if omega == 0:
            raise ValueError("Angular frequency omega cannot be zero.")
        if epsilon <= 0:
            raise ValueError("Time step epsilon must be positive.")
        
        self.omega = omega
        self.epsilon = epsilon
        self.x0 = x0
        self.v0 = v0
        self.phi = phi
        
        self.x_prev = x0 * np.cos(phi) + (v0 / omega) * np.sin(phi)
        self.x_curr = x0 * np.cos(omega * epsilon + phi) + (v0 / omega) * np.sin(omega * epsilon + phi)
        self.step_count = 1
        self.start_time = time.time()
        
    def reset(self):
        """Reset oscillator to initial conditions"""
        self.x_prev = self.x0 * np.cos(self.phi) + (self.v0 / self.omega) * np.sin(self.phi)
        self.x_curr = self.x0 * np.cos(self.omega * self.epsilon + self.phi) + (self.v0 / self.omega) * np.sin(self.omega * self.epsilon + self.phi)
        self.step_count = 1
        self.start_time = time.time()
    
    def next_position(self) -> float:
        """
        Compute next position using exact discretization
        
        Returns:
            float: Next position x_{n+1}
        """
        x_next = 2 * np.cos(self.omega * self.epsilon) * self.x_curr - self.x_prev
        self.x_prev = self.x_curr
        self.x_curr = x_next
        self.step_count += 1
        return x_next
    
    def next_position_with_timestamp(self) -> Tuple[float, float]:
        """
        Compute next position with timestamp
        
        Returns:
            Tuple[float, float]: (timestamp, position)
        """
        timestamp = time.time()
        position = self.next_position()
        return timestamp, position
    
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
    
    def get_positions_with_timestamps(self, num_steps: int) -> Generator[Tuple[float, float], None, None]:
        """
        Generate stream of (timestamp, position) pairs
        
        Args:
            num_steps: Number of data points to generate
            
        Yields:
            Tuple[float, float]: (timestamp, position) pairs
        """
        for _ in range(num_steps):
            yield self.next_position_with_timestamp()
    
    def get_positions_with_time(self, num_steps: int) -> Generator[Tuple[float, float], None, None]:
        """
        Generate stream of (discrete_time, position) pairs
        
        Args:
            num_steps: Number of data points to generate
            
        Yields:
            Tuple[float, float]: (t_n, x_n) pairs where t_n = n*epsilon
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
    
    def get_infinite_stream_with_timestamps(self) -> Generator[Tuple[float, float], None, None]:
        """
        Generate infinite stream of (timestamp, position) pairs
        
        Yields:
            Tuple[float, float]: (timestamp, position) pairs (infinite)
        """
        while True:
            yield self.next_position_with_timestamp()
    
    def get_infinite_stream_with_discrete_time(self) -> Generator[Tuple[float, float], None, None]:
        """
        Generate infinite stream of (discrete_time, position) pairs
        
        Yields:
            Tuple[float, float]: (t_n, x_n) pairs where t_n = n*epsilon (infinite)
        """
        step = 0
        while True:
            t_n = step * self.epsilon
            x_n = self.next_position()
            yield t_n, x_n
            step += 1
    
    def get_batch(self, num_steps: int) -> np.ndarray:
        """
        Generate batch of positions as numpy array
        
        Args:
            num_steps: Number of positions to generate
            
        Returns:
            np.ndarray: Array of position values
        """
        return np.array([self.next_position() for _ in range(num_steps)])
    
    def get_batch_with_timestamps(self, num_steps: int) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate batch of positions with timestamps
        
        Args:
            num_steps: Number of positions to generate
            
        Returns:
            Tuple[np.ndarray, np.ndarray]: (timestamps, positions) arrays
        """
        timestamps = []
        positions = []
        for _ in range(num_steps):
            timestamp, position = self.next_position_with_timestamp()
            timestamps.append(timestamp)
            positions.append(position)
        return np.array(timestamps), np.array(positions)
    
    @property
    def current_state(self) -> dict:
        """Get current oscillator state"""
        return {
            'x_prev': self.x_prev,
            'x_curr': self.x_curr,
            'step_count': self.step_count,
            'omega': self.omega,
            'epsilon': self.epsilon,
            'phi': self.phi,
            'start_time': self.start_time,
            'current_time': time.time()
        }


def create_test_stream(omega: float = 1.0, epsilon: float = 0.01, 
                      x0: float = 1.0, v0: float = 0.0, phi: float = 0.0) -> np.ndarray:
    """
    Convenience function to create test data for SKA learning
    """
    stream = HarmonicOscillatorStream(omega=omega, epsilon=epsilon, x0=x0, v0=v0, phi=phi)
    return stream.get_batch(num_steps=1000)


def create_test_stream_with_timestamps(omega: float = 1.0, epsilon: float = 0.01, 
                                     x0: float = 1.0, v0: float = 0.0, phi: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    Convenience function to create test data with timestamps for SKA learning
    """
    stream = HarmonicOscillatorStream(omega=omega, epsilon=epsilon, x0=x0, v0=v0, phi=phi)
    return stream.get_batch_with_timestamps(num_steps=1000)


def demo_ska_integration():
    """Demonstrate how to use with SKA learning process"""
    print("SKA Integration Demo")
    print("=" * 30)
    
    stream = HarmonicOscillatorStream(omega=2.0, epsilon=0.01, x0=1.0, v0=0.0, phi=np.pi/4)
    print(f"Parameters: ω=2.0 rad/s, ε=0.01 s, x₀=1.0, v₀=0.0, φ={np.pi/4:.3f} rad")
    print("Generating position stream with timestamps for SKA learning...")
    print("Format: timestamp, position")
    print("-" * 40)
    
    for i, (timestamp, position) in enumerate(stream.get_positions_with_timestamps(20)):
        print(f"Step {i:2d}: {timestamp:.6f}, {position:8.6f}")
    
    print("\nBatch generation with timestamps example:")
    stream.reset()
    timestamps, positions = stream.get_batch_with_timestamps(100)
    print(f"Generated batch shapes: timestamps={timestamps.shape}, positions={positions.shape}")
    print(f"Time range: {timestamps.min():.6f} to {timestamps.max():.6f}")
    print(f"Position stats: min={positions.min():.6f}, max={positions.max():.6f}, std={positions.std():.6f}")


def continuous_stream():
    """Run continuous data stream for SKA learning"""
    print("SKA Harmonic Oscillator - Physics Real-Time Stream")
    print("Real time = mathematical time of oscillator")
    print("=" * 60)
    
    # Parameters
    omega = 0.1      # Angular frequency (rad/s)
    x0 = 1.0         # Initial position
    v0 = 0.0         # Initial velocity
    phi = np.pi/4    # Phase (radians)
    
    print(f"ω = {omega} rad/s (period ≈ {2*np.pi/omega:.3f} s)")
    print(f"Initial: x₀ = {x0}, v₀ = {v0}, φ = {phi:.3f} rad ({phi*180/np.pi:.1f}°)")
    print("\nPhysics real-time stream (press Ctrl+C to stop)...")
    print("Format: step, timestamp, elapsed_time, position")
    print("-" * 50)
    
    start_time = time.time()
    step = 0
    
    try:
        while True:
            # Current timestamp and elapsed time
            timestamp = time.time()
            elapsed_time = timestamp - start_time
            
            # Compute analytical position at current real time
            position = x0 * np.cos(omega * elapsed_time + phi) + (v0 / omega) * np.sin(omega * elapsed_time + phi)
            
            print(f"{step:6d}, {timestamp:.6f}, {elapsed_time:8.3f}, {position:12.8f}")
            step += 1
            time.sleep(0.1)  # Update every 100ms for reasonable display rate
            
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        cycles_completed = elapsed_time * omega / (2 * np.pi)
        print(f"\nStopped after {elapsed_time:.1f} seconds")
        print(f"Completed {cycles_completed:.2f} oscillation cycles")


def discrete_time_demo():
    """Discrete time streaming demo"""
    print("SKA data stream with discrete time (press Ctrl+C to stop)")
    print("=" * 60)
    
    stream = HarmonicOscillatorStream(omega=2.0, epsilon=0.05, phi=np.pi/6)
    
    try:
        for discrete_time, position in stream.get_infinite_stream_with_discrete_time():
            print(f"{discrete_time:.6f}, {position:.6f}")
            if discrete_time > 5.0:  # Stop after 5 seconds of discrete time
                break
    except KeyboardInterrupt:
        print("\nDiscrete time stream stopped.")


if __name__ == "__main__":
    continuous_stream()
    # Uncomment for other demos:
    # demo_ska_integration()
    # discrete_time_demo()