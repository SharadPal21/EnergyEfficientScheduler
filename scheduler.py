from collections import deque
import matplotlib.pyplot as plt
import psutil
import time

class Process:
    def __init__(self, name, burst_time, power):
        self.name = name
        self.burst_time = burst_time
        self.power = power  # Power levels: Low, Medium, High

def visualize_energy_usage(processes, energy_data):
    process_names = [p.name for p in processes]
    energy_values = list(energy_data.values())

    plt.bar(process_names, energy_values, color=['green', 'orange', 'red', 'blue'])
    plt.title("Energy Consumption Per Process")
    plt.xlabel("Processes")
    plt.ylabel("Energy Units")
    plt.show()

def visualize_cpu_usage():
    usage = []
    timestamps = []

    print("\nTracking CPU Usage in Real-Time (for visualization)...")
    for _ in range(20):
        cpu_percent = psutil.cpu_percent(interval=0.5)
        usage.append(cpu_percent)
        timestamps.append(time.strftime("%H:%M:%S"))
    
    plt.plot(timestamps, usage, label='CPU Usage (%)', color='blue', marker='o')
    plt.title('CPU Usage Over Time')
    plt.xlabel('Time')
    plt.ylabel('CPU Usage (%)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def energy_efficient_rr(processes, time_quantum):
    power_map = {"Low": 1, "Medium": 2, "High": 3}

    queue = deque(processes)
    total_energy = 0  
    energy_data = {p.name: 0 for p in processes}  

    while queue:
        process = queue.popleft()

        execution_time = min(process.burst_time, time_quantum)  
        print(f"Executing {process.name} for {execution_time} units.")

        # Correct Energy Calculation
        energy_used = execution_time * power_map[process.power]
        total_energy += energy_used
        energy_data[process.name] += energy_used
        print(f"{process.name} consumed {energy_used} units. (Total Energy: {total_energy})")

        process.burst_time -= execution_time

        if process.burst_time > 0:
            queue.append(process)
        else:
            print(f"{process.name} completed.")

        if not queue:
            print("CPU entering low-power mode...")

    print(f"\nTotal Energy Consumed: {total_energy} units")

    # Visualizations
    visualize_energy_usage(processes, energy_data)
    visualize_cpu_usage()

# Sample Processes with Correct Burst Times
process_list = [
    Process("P1", 4, "Low"),
    Process("P2", 4, "Medium"),
    Process("P3", 4, "High"),
    Process("P4", 4, "Low")
]

# Define Time Quantum
time_quantum = 4
energy_efficient_rr(process_list, time_quantum)
