# Automated Script Scheduler

A Python-based automation tool that monitors system time and automatically executes multiple Python scripts and Jupyter notebooks at a predefined schedule. The system uses subprocess execution to run scripts sequentially and capture outputs and errors, enabling reliable automation of data pipelines, report generation, and workflow orchestration.

## 🚀 Features

- ⏱️ Time-based automation for running scripts
- 🐍 Executes both Python (.py) and Jupyter Notebook (.ipynb) files
- 📊 Captures execution logs, outputs, and errors
- 🔄 Sequential execution with configurable delays
- ⚙️ Simple configuration for scripts and scheduled time
- 🛠️ Useful for data pipelines, automation workflows, and scheduled reporting
  
## 🛠️ Tech Stack

- Python
- Subprocess
- Jupyter nbconvert
- Time-based scheduling

## 📌 Use Cases

- Automated data extraction pipelines
- Scheduled report generation
- Running machine learning pipelines
- Batch processing automation
- Data workflow orchestration

## 📂 Project Structure

- automation-script-scheduler/
- ├── script_scheduler.py
- ├── README.md
- └── requirements.txt
  
## ▶️ How It Works

- The scheduler continuously checks the system time.
- When the configured target time matches the current time, execution begins.
- The system runs each script sequentially.
- Outputs and errors are logged for monitoring and debugging.

## 👨‍💻 Author

#### Vrushank Dhande
#### Data Analyst | Machine Learning Enthusiast | Automation Developer
