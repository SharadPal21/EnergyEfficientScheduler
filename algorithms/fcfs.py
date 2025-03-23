# fcfs.py — First-Come, First-Served Algorithm with Console Input
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import visualize_gantt_chart, calculate_metrics, Process



# FCFS Algorithm Function
def fcfs_scheduling():
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

    # Sorting processes by arrival time for FCFS
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    gantt_chart = []
    completion_times = {}

    print("\n--- FCFS Scheduling ---")
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # Handle idle CPU time

        gantt_chart.append((process.name, current_time, current_time + process.burst_time))
        completion_times[process.name] = current_time + process.burst_time

        print(f"{process.name} executed from {current_time} to {current_time + process.burst_time}")
        current_time += process.burst_time

    visualize_gantt_chart(gantt_chart, "FCFS Scheduling")
    calculate_metrics(processes, completion_times)

# Main Execution
if __name__ == "__main__":
    fcfs_scheduling()
