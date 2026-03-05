"""
Automated Script Scheduler

This script continuously monitors the system time and triggers a list of
Python scripts and Jupyter notebooks when a specified target time is reached.

Features
--------
- Supports execution of both `.py` and `.ipynb` files
- Uses `subprocess` for isolated execution
- Prints execution logs and errors
- Runs scripts sequentially with delay between executions

Author: Vrushank Dhande
"""

import time
import subprocess
from datetime import datetime

# ==============================
# CONFIGURATION
# ==============================

TARGET_TIME = "02:50:00"  # Format: HH:MM:SS (24-hour)

JUPYTER_PATH = r""  ## your jupyter path here, e.g. C:\Users\Admin\anaconda3\Scripts\jupyter.exe

SCRIPTS = [
    "main1.py",
    "main2.ipynb",
    "main3.py"
]

DELAY_BETWEEN_SCRIPTS = 10


# ==============================
# SCRIPT EXECUTION FUNCTION
# ==============================

def run_script(script_name):
    """
    Execute a Python script or Jupyter notebook.
    """

    print(f"\nProcessing: {script_name}")

    try:
        if script_name.endswith(".ipynb"):
            print("Detected Jupyter Notebook")

            result = subprocess.run(
                [
                    JUPYTER_PATH,
                    "nbconvert",
                    "--to",
                    "notebook",
                    "--execute",
                    "--inplace",
                    script_name
                ],
                capture_output=True,
                text=True
            )

        else:
            print("Detected Python Script")

            result = subprocess.run(
                ["python", script_name],
                capture_output=True,
                text=True
            )

        print(f"\nOutput of {script_name}:\n{result.stdout}")

        if result.stderr:
            print(f"\nError in {script_name}:\n{result.stderr}")

        print(f"Completed: {script_name}")

    except Exception as e:
        print(f"Execution failed for {script_name}: {e}")


# ==============================
# MAIN SCHEDULER LOOP
# ==============================

def start_scheduler():
    """
    Continuously checks system time and runs scripts at TARGET_TIME.
    """

    print("Scheduler started...")
    print(f"Target Time: {TARGET_TIME}")

    while True:

        current_time = time.strftime("%H:%M:%S")

        print("Current Time:", current_time)

        if current_time == TARGET_TIME:

            print(f"\nTarget time matched: {TARGET_TIME}")
            print("Starting script execution...\n")

            for script in SCRIPTS:

                run_script(script)
                time.sleep(DELAY_BETWEEN_SCRIPTS)

            print("\nAll scripts completed.\n")

            # Prevent multiple executions in same second
            time.sleep(60)

        time.sleep(1)


# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    start_scheduler()