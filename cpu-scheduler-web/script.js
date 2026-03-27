// 📦 Global State
let processes = [];
let chart = null;

// ➕ Add Process
function addProcess() {
  const name = document.getElementById("name").value || `P${processes.length + 1}`;
  const arrival = parseInt(document.getElementById("arrival").value);
  const burst = parseInt(document.getElementById("burst").value);
  const priority = parseInt(document.getElementById("priority").value) || 0;

  if (isNaN(arrival) || isNaN(burst)) {
    alert("Please enter valid Arrival and Burst times");
    return;
  }

  processes.push({ name, arrival, burst, priority });
  renderTable();
  clearInputs();
}

// 🧹 Clear Inputs
function clearInputs() {
  document.getElementById("name").value = "";
  document.getElementById("arrival").value = "";
  document.getElementById("burst").value = "";
  document.getElementById("priority").value = "";
}

// 🗑 Clear All Processes
function clearProcesses() {
  processes = [];
  renderTable();
  document.getElementById("metrics").innerHTML = "Cleared.";
  if (chart) chart.destroy();
}

// 📋 Render Table
function renderTable() {
  const tbody = document.querySelector("#processTable tbody");
  tbody.innerHTML = "";

  processes.forEach(p => {
    const row = `<tr>
      <td>${p.name}</td>
      <td>${p.arrival}</td>
      <td>${p.burst}</td>
      <td>${p.priority}</td>
    </tr>`;
    tbody.innerHTML += row;
  });
}

// ▶ Run Scheduler
function runScheduler() {
  if (processes.length === 0) {
    alert("Add at least one process");
    return;
  }

  const algo = document.getElementById("algorithm").value;
  const quantum = parseInt(document.getElementById("quantum").value) || 2;

  let schedule = [];

  if (algo === "fcfs") schedule = fcfs([...processes]);
  else if (algo === "sjf") schedule = sjf([...processes]);
  else if (algo === "priority") schedule = priorityScheduling([...processes]);
  else if (algo === "rr") schedule = roundRobin([...processes], quantum);

  displayResults(schedule);
}

// 🔹 FCFS
function fcfs(ps) {
  ps.sort((a, b) => a.arrival - b.arrival);
  let time = 0;
  let result = [];

  ps.forEach(p => {
    if (time < p.arrival) time = p.arrival;

    let start = time;
    let end = time + p.burst;

    result.push({ name: p.name, start, end, burst: p.burst, arrival: p.arrival });
    time = end;
  });

  return result;
}

// 🔹 SJF (Non-preemptive)
function sjf(ps) {
  let time = 0;
  let completed = [];
  let result = [];

  while (completed.length < ps.length) {
    let ready = ps.filter(p => p.arrival <= time && !completed.includes(p));

    if (ready.length === 0) {
      time++;
      continue;
    }

    ready.sort((a, b) => a.burst - b.burst);
    let p = ready[0];

    let start = time;
    let end = time + p.burst;

    result.push({ name: p.name, start, end, burst: p.burst, arrival: p.arrival });

    completed.push(p);
    time = end;
  }

  return result;
}

// 🔹 Priority Scheduling
function priorityScheduling(ps) {
  let time = 0;
  let completed = [];
  let result = [];

  while (completed.length < ps.length) {
    let ready = ps.filter(p => p.arrival <= time && !completed.includes(p));

    if (ready.length === 0) {
      time++;
      continue;
    }

    ready.sort((a, b) => a.priority - b.priority);
    let p = ready[0];

    let start = time;
    let end = time + p.burst;

    result.push({ name: p.name, start, end, burst: p.burst, arrival: p.arrival });

    completed.push(p);
    time = end;
  }

  return result;
}

// 🔹 Round Robin
function roundRobin(ps, quantum) {
  let time = 0;
  let queue = ps.map(p => ({ ...p, remaining: p.burst }));
  let result = [];

  while (queue.length > 0) {
    let p = queue.shift();

    if (p.arrival > time) time = p.arrival;

    let start = time;
    let exec = Math.min(quantum, p.remaining);

    time += exec;
    p.remaining -= exec;

    result.push({
      name: p.name,
      start,
      end: time,
      burst: p.burst,
      arrival: p.arrival
    });

    if (p.remaining > 0) {
      queue.push(p);
    }
  }

  return result;
}

// 📊 Display Results
function displayResults(results) {
  const ctx = document.getElementById("ganttChart").getContext("2d");

  // Destroy old chart
  if (chart) chart.destroy();

  const labels = results.map(r => `${r.name} (${r.start}-${r.end})`);
  const data = results.map(r => r.end - r.start);
  const colors = results.map((_, i) => `hsl(${i * 60}, 70%, 60%)`);

  chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [{
        label: "Gantt Chart",
        data,
        backgroundColor: colors
      }]
    },
    options: {
      indexAxis: "y",
      responsive: true,
      plugins: {
        legend: { display: false }
      },
      scales: {
        x: {
          beginAtZero: true,
          title: {
            display: true,
            text: "Time"
          }
        }
      }
    }
  });

  // 📈 Calculate Metrics
  let completion = {};

  results.forEach(r => {
    completion[r.name] = r.end;
  });

  let totalWT = 0;
  let totalTAT = 0;

  processes.forEach(p => {
    let ct = completion[p.name];
    let tat = ct - p.arrival;
    let wt = tat - p.burst;

    totalWT += wt;
    totalTAT += tat;
  });

  let avgWT = (totalWT / processes.length).toFixed(2);
  let avgTAT = (totalTAT / processes.length).toFixed(2);

  document.getElementById("metrics").innerHTML = `
    <b>Average Waiting Time:</b> ${avgWT} <br>
    <b>Average Turnaround Time:</b> ${avgTAT}
  `;
}

// 🔄 Toggle Quantum Input
document.getElementById("algorithm").addEventListener("change", function () {
  const isRR = this.value === "rr";
  document.getElementById("quantum").style.display = isRR ? "block" : "none";
});