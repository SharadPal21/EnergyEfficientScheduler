from collections import deque
import time

class Process:
    def __init__(self, name, burst_time, power):
        self.name = name
        self.burst_time = burst_time
        self.power = power  # Power levels: Low, Medium, High

def energy_efficient_rr(processes, time_quantum):
    power_map = {"Low": 1, "Medium": 2, "High": 3}

    queue = deque(processes)
    total_energy = 0  # Track total energy consumption

    while queue:
        process = queue.popleft()

        # Track power value
        print(f"{process.name} has power level: {power_map[process.power]}")

        execution_time = min(process.burst_time, time_quantum)
        print(f"Executing {process.name} for {execution_time} units.")

        # Energy calculation with detailed tracking
        energy_used = execution_time * power_map[process.power]
        total_energy += energy_used
        print(f"{process.name} consumed {energy_used} energy units this cycle. (Total Energy: {total_energy})")

        process.burst_time -= execution_time

        if process.burst_time > 0:
            queue.append(process)
        else:
            print(f"{process.name} completed.")

        # Enter low-power mode if no process remains
        if not queue:
            print("CPU entering low-power mode...")

    print(f"\nTotal Energy Consumed: {total_energy} units")

# Sample Processes (Ensure Correct Values)
process_list = [
    Process("P1", 8, "Low"),    # Power = 1
    Process("P2", 4, "Medium"), # Power = 2
    Process("P3", 6, "High"),   # Power = 3
    Process("P4", 3, "Low")     # Power = 1
]

# Define Time Quantum
time_quantum = 4
energy_efficient_rr(process_list, time_quantum)