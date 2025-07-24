#!/usr/bin/env python3
"""
oscillator_stream.py
SKA Harmonic Oscillator Stream Generator
Provides real-time position data stream for SKA learning process
Using exact discretization: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0
Version: 2025-07-17-User-Fixed
"""

import numpy as np
import time
from typing import Generator, Tuple

class HarmonicOscillatorStream:
    def __init__(self, omega: float = 1.0, epsilon: float = 0.01, 
                 x0: float = 1.0, v0: float = 0.0, phi: float = 0.0):
        try:
            if omega == 0:
                raise ValueError("Angular frequency omega cannot be zero.")
            if epsilon <= 0:
                raise ValueError("Time step epsilon must be positive.")
            
            self.omega = omega
            self.epsilon = epsilon
            self.x0 = x0
            self.v0 = v0
            self.phi = phi
            
            # Initialize positions at t=0
            self.x_prev = x0 * np.cos(phi) + (v0 / omega) * np.sin(phi)
            self.x_curr = self.x_prev
            self.step_count = 0
            self.start_time = time.time()
        except Exception as e:
            print(f"Error initializing HarmonicOscillatorStream: {e}")
            raise
    
    def next_position(self) -> float:
        try:
            x_next = 2 * np.cos(self.omega * self.epsilon) * self.x_curr - self.x_prev
            self.x_prev = self.x_curr
            self.x_curr = x_next
            self.step_count += 1
            return x_next
        except Exception as e:
            print(f"Error computing next position: {e}")
            raise
    
    def next_position_with_timestamp(self) -> Tuple[float, float]:
        try:
            timestamp = time.time()
            position = self.next_position()
            return timestamp, position
        except Exception as e:
            print(f"Error computing position with timestamp: {e}")
            raise
    
    def get_infinite_stream_with_timestamps(self) -> Generator[Tuple[float, float], None, None]:
        try:
            while True:
                yield self.next_position_with_timestamp()
        except Exception as e:
            print(f"Error in infinite stream with timestamps: {e}")
            raise
    
    @property
    def current_state(self) -> dict:
        try:
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
        except Exception as e:
            print(f"Error getting current state: {e}")
            raise

def continuous_stream():
    try:
        print("Starting oscillator_stream.py (Version: 2025-07-17-User-Fixed)...")
        print("SKA Harmonic Oscillator - Physics Real-Time Stream")
        print("Exact discretization: x_{n+1} - 2cos(ωε)x_n + x_{n-1} = 0")
        print("=" * 60)
        
        # Parameters
        omega = 0.1
        epsilon = 0.01
        x0 = 1.0
        v0 = 0.0
        phi = np.pi/4
        
        print(f"ω = {omega} rad/s (period ≈ {2*np.pi/omega:.3f} s)")
        print(f"ε = {epsilon} s")
        print(f"Initial: x₀ = {x0}, v₀ = {v0}, φ = {phi:.3f} rad ({phi*180/np.pi:.1f}°)")
        if omega * epsilon < 0.001:
            print(f"Warning: Small ωε product may cause slow oscillations (period ~{2*np.pi/omega:.1f} s).")
        print("\nPhysics real-time stream (press Ctrl+C to stop)...")
        print("Format: step, timestamp, physical_time, position")
        print("-" * 50)
        
        stream = HarmonicOscillatorStream(omega=omega, epsilon=epsilon, x0=x0, v0=v0, phi=phi)
        
        step = 0
        start_time = time.time()
        last_position = stream.x_curr
        
        while True:
            # Calculate exact target time for this step
            target_time = start_time + (step * epsilon)
            
            # Wait until we reach the exact target time
            current_time = time.time()
            if current_time < target_time:
                time.sleep(target_time - current_time)
            
            # Take timestamp at exact target time
            timestamp = time.time()
            position = stream.next_position()
            physical_time = timestamp - start_time
            
            print(f"{step:6d}, {timestamp:.6f}, {physical_time:11.6f}, {position:12.8f}")
            if step == 0:
                print(f"Debug: physical_time = {physical_time:.6f}, step * epsilon = {step * epsilon:.6f}")
            
            if step % 1000 == 0 and step > 0:
                position_change = abs(position - last_position)
                timing_error = abs(physical_time - (step * epsilon))
                print(f"Debug: Position change over {step} steps: {position_change:.8f}")
                print(f"Debug: Timing error (should be {step * epsilon:.3f}s): {timing_error:.6f}s")
                last_position = position
            
            step += 1
            
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        cycles_completed = elapsed_time * omega / (2 * np.pi)
        print(f"\nStopped after {step} steps")
        print(f"Real time elapsed: {elapsed_time:.1f} seconds")
        print(f"Completed {cycles_completed:.2f} oscillation cycles")
        print("Final state:", stream.current_state)
    except Exception as e:
        print(f"Error in continuous_stream: {e}")
        raise

if __name__ == "__main__":
    try:
        print("Script loaded, attempting to start (Version: 2025-07-17-User-Fixed)...")
        continuous_stream()
    except Exception as e:
        print(f"Failed to start script: {e}")
        raise