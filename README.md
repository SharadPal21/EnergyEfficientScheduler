CPU Scheduling Simulator

This project is a comprehensive CPU Scheduling Simulator that implements four key scheduling algorithms:

First-Come, First-Served (FCFS)Shortest Job First (SJF)Priority SchedulingRound Robin

The simulator provides a menu-based interface for easy selection and visualizes each algorithm's execution with a Gantt Chart and performance metrics like Average Waiting Time (AWT) and Average Turnaround Time (ATAT).

Features

User Input: Supports entering process details directly in the console.

Gantt Chart Visualization: Displays the process execution timeline.

Detailed Performance Metrics: Calculates AWT and ATAT for each algorithm.

Robust Error Handling: Ensures valid inputs are accepted.

How to Run the Project

Step 1: Clone the Repository :git clone https://github.com/SharadPal21/EnergyEfficientScheduler.git

cd EnergyEfficientScheduler

Step 2: Install the Required Packages : pip install matplotlib pandas numpy

Step 3: Run the Simulator
python scheduler.py

Step 4: Select an Algorithm
    From the menu, choose:
        1. First-Come, First-Served (FCFS)
        2. Shortest Job First (SJF)
        3. Priority Scheduling
        4. Round Robin
        5. Exit

Step 5: Follow the Prompts
    Enter process details such as:

        Arrival Time

        Burst Time

        Priority

        Power Level

Step 6: View Results

The system will display:
Gantt ChartAverage Waiting Time (AWT)Average Turnaround Time (ATAT)

Sample Commands for Execution

Run each algorithm independently:
python algorithms/fcfs.py
python algorithms/sjf.py
python algorithms/priority.py
python algorithms/round_robin.py

Project Structure
EnergyEfficientScheduler/
├── algorithms/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   ├── round_robin.py
│
├── utils.py
├── scheduler.py
├── README.md

GitHub Workflow

7+ Commits: Each feature and improvement was committed with clear messages.Branching Strategy: Each algorithm was developed in its own branch and merged into main after testing.Public Repository: Accessible to anyone for evaluation and review.

Support

For any questions or improvements, feel free to raise an issue or contribute directly.
