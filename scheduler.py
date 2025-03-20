from collections import deque
import time

class Process:
    def __init__(self, name, burst_time, power):
        self.name = name
        self.burst_time = burst_time
        self.power = power  # Power levels: Low, Medium, High

def energy_efficient_rr(processes, time_quantum):
    power_map = {"Low": 1, "Medium": 2, "High": 3}

    # Sort processes by power consumption (Low < Medium < High)
    processes.sort(key=lambda x: power_map[x.power])

    queue = deque(processes)
    total_energy = 0  # Track total energy consumption

    while queue:
        process = queue.popleft()

        execution_time = min(process.burst_time, time_quantum)
        print(f"Executing {process.name} for {execution_time} units.")
        total_energy += execution_time * power_map[process.power]
        process.burst_time -= execution_time

        if process.burst_time > 0:
            queue.append(process)  # Add back to the queue
        else:
            print(f"{process.name} completed.")

        # Enter low-power mode if the queue is empty
        if not queue:
            print("CPU entering low-power mode...")

    print(f"\nTotal Energy Consumed: {total_energy} units")

# Sample Processes
process_list = [
    Process("P1", 8, "Low"),
    Process("P2", 4, "Medium"),
    Process("P3", 6, "High"),
    Process("P4", 3, "Low")
]

# Define Time Quantum
time_quantum = 4
energy_efficient_rr(process_list, time_quantum)
