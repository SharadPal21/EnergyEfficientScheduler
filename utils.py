import matplotlib.pyplot as plt

# Process Class for Scheduling Algorithms
class Process:
    def __init__(self, name, arrival_time, burst_time, priority, power):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.power = power  

# Visualizing Gantt Chart
def visualize_gantt_chart(gantt_chart, title):
    plt.figure(figsize=(10, 4))
    colors = ['green', 'orange', 'red', 'blue', 'purple']

    for i, (process, start, end) in enumerate(gantt_chart):
        plt.barh(y=0, left=start, width=end-start, color=colors[i % len(colors)])
        plt.text((start + end) / 2, 0, process, ha='center', va='center', fontsize=10, color='white')

    plt.xlabel('Time')
    plt.title(title)
    plt.yticks([])  
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.show()

# Performance Metrics Calculation
def calculate_metrics(processes, completion_times):
    waiting_times = []
    turnaround_times = []

    for process in processes:
        completion_time = completion_times[process.name]
        waiting_time = completion_time - process.arrival_time - process.burst_time
        turnaround_time = completion_time - process.arrival_time

        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)

    avg_waiting_time = sum(waiting_times) / len(processes)
    avg_turnaround_time = sum(turnaround_times) / len(processes)

    print(f"\nAverage Waiting Time (AWT): {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time (ATAT): {avg_turnaround_time:.2f}")
