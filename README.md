# Energy-Efficient Scheduler
This project implements an **Energy-Efficient CPU Scheduling Algorithm** using the **Round Robin Scheduling Algorithm**.
The goal is to minimize energy consumption while efficiently handling multiple processes.

### Features
Prioritizes low-energy-consuming processes
Introduces a low-power mode when the CPU is idle
Tracks and visualizes total energy consumption per process
Displays real-time CPU performance using `psutil`

## How to Run
1. **Install Dependencies**
   Run the following command to install required libraries: pip install matplotlib psutil

2. **Clone the Repository**
git clone https://github.com/SharadPal21/EnergyEfficientScheduler.git

3. **Navigate to the Project Folder**
cd EnergyEfficientScheduler

4. **Run the Code**
python scheduler.py

## Sample Output
Executing P1 for 4 units.
P1 consumed 4 units. (Total Energy: 4)
Executing P2 for 4 units.
P2 consumed 8 units. (Total Energy: 12)
Executing P3 for 4 units.
P3 consumed 12 units. (Total Energy: 24)
Executing P4 for 4 units.
P4 consumed 4 units. (Total Energy: 28)
CPU entering low-power mode...
Total Energy Consumed: 28 units

## Visualizations
- **Energy Consumption Bar Chart:** Displays energy usage for each process.
- **CPU Usage Graph:** Tracks real-time CPU performance during scheduling.

## Future Enhancements
- Introduce **Dynamic Time Quantum** for improved efficiency.
- Add a **Priority Queue** to prioritize high-priority tasks.
- Implement a **GUI Interface** for better user experience.

## Author
**Sharad Pal**
Lovely Professional University
India
