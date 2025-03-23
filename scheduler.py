# scheduler.py — Menu-Based CPU Scheduling Simulator
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.priority import priority_scheduling
from algorithms.round_robin import round_robin_scheduling

def main():
    while True:
        print("\n🔹 CPU Scheduling Simulator 🔹")
        print("1. First-Come, First-Served (FCFS)")
        print("2. Shortest Job First (SJF)")
        print("3. Priority Scheduling")
        print("4. Round Robin")
        print("5. Exit")

        # Input validation for menu selection
        try:
            choice = int(input("Select an algorithm (1-5): "))
            if choice not in [1, 2, 3, 4, 5]:
                print("❌ Invalid choice. Please select a valid option (1-5).")
                continue
        except ValueError:
            print("❌ Invalid input. Please enter a number between 1-5.")
            continue

        if choice == 1:
            fcfs_scheduling()
        elif choice == 2:
            sjf_scheduling()
        elif choice == 3:
            priority_scheduling()
        elif choice == 4:
            round_robin_scheduling()
        elif choice == 5:
            print("✅ Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
