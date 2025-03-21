# Energy Efficient Scheduler

This project implements an **Energy-Efficient CPU Scheduling Algorithm** using Round Robin logic to minimize energy consumption.

## Features
✅ Prioritizes low-energy-consuming processes  
✅ Introduces a low-power mode for idle CPU states  
✅ Tracks total energy consumption per process  

## How It Works
The algorithm follows these steps:
1. Each process is assigned a **burst time** and **power level** (Low, Medium, or High).
2. Round Robin scheduling is used to execute processes in cycles of fixed time (called the **Time Quantum**).
3. Energy consumption is calculated using: Energy Used = Execution Time × Power Value
4. A **low-power mode** is triggered when no processes are running.

## Sample Output

## How to Run
1. Clone this repository: git clone https://github.com/SharadPal21/EnergyEfficientScheduler.git
2. Navigate to the project folder: cd EnergyEfficientScheduler
3. Run the code: python scheduler.py

## Future Enhancements
🔹 Dynamic time quantum for improved efficiency  
🔹 Real-time process arrival simulation  

## Author
**Sharad Pal**

