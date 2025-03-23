# sjf.py — Shortest Job First (SJF) Algorithm with Console Input
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import visualize_gantt_chart, calculate_metrics, Process

# SJF Algorithm Function
def sjf_scheduling():
    # Taking user input for processes
    n = int(input("Enter the number of processes: "))
    processes = []

    for i in range(n):
        name = f"P{i+1}"
        
        # Input Validation
        while True:
            try:
                arrival_time = int(input(f"Enter arrival time for {name}: "))
                burst_time = int(input(f"Enter burst time for {name}: "))
                priority = int(input(f"Enter priority for {name} (Lower value = Higher priority): "))
                if arrival_time < 0 or burst_time <= 0 or priority < 0:
                    raise ValueError("Values must be positive integers.")
                break
            except ValueError:
                print("Invalid input. Please enter positive integers only.")
        
        power = input(f"Enter power level for {name} (Low/Medium/High): ").strip().capitalize()
        while power not in ["Low", "Medium", "High"]:
            print("Invalid power level. Choose from Low, Medium, or High.")
            power = input(f"Enter power level for {name} (Low/Medium/High): ").strip().capitalize()

        processes.append(Process(name, arrival_time, burst_time, priority, power))

    # Sorting processes based on arrival time and burst time
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

    current_time = 0
    gantt_chart = []
    completion_times = {}

    print("\n--- SJF Scheduling ---")
    remaining_processes = processes.copy()

    while remaining_processes:
        # Filter available processes
        available_processes = [p for p in remaining_processes if p.arrival_time <= current_time]

        if not available_processes:
            # If no process is available, jump to the next arrival time
            current_time = min(p.arrival_time for p in remaining_processes)
            continue

        # Select the process with the shortest burst time
        shortest_process = min(available_processes, key=lambda x: x.burst_time)
        remaining_processes.remove(shortest_process)

        gantt_chart.append((shortest_process.name, current_time, current_time + shortest_process.burst_time))
        completion_times[shortest_process.name] = current_time + shortest_process.burst_time

        print(f"{shortest_process.name} executed from {current_time} to {current_time + shortest_process.burst_time}")
        current_time += shortest_process.burst_time

    visualize_gantt_chart(gantt_chart, "SJF Scheduling")
    calculate_metrics(processes, completion_times)

# Main Execution
if __name__ == "__main__":
    sjf_scheduling()
