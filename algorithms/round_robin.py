# round_robin.py — Round Robin Algorithm with Console Input
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import visualize_gantt_chart, calculate_metrics, Process
from collections import deque

# Round Robin Algorithm Function
def round_robin_scheduling():
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

    # Time Quantum Input
    while True:
        try:
            time_quantum = int(input("Enter the time quantum: "))
            if time_quantum <= 0:
                raise ValueError("Time quantum must be a positive integer.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer for the time quantum.")

    # Sorting processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    queue = deque(processes)
    gantt_chart = []
    completion_times = {}

    print("\n--- Round Robin Scheduling ---")
    while queue:
        process = queue.popleft()

        # Execute the process for the given time quantum or remaining burst time
        execution_time = min(process.burst_time, time_quantum)
        gantt_chart.append((process.name, current_time, current_time + execution_time))
        process.burst_time -= execution_time

        if process.burst_time > 0:
            # Process still has remaining time — re-add it to the queue
            queue.append(process)
        else:
            # Process completed
            completion_times[process.name] = current_time + execution_time
            print(f"{process.name} executed from {current_time} to {current_time + execution_time} (Completed)")

        current_time += execution_time

    visualize_gantt_chart(gantt_chart, "Round Robin Scheduling")
    calculate_metrics(processes, completion_times)

# Main Execution
if __name__ == "__main__":
    round_robin_scheduling()
