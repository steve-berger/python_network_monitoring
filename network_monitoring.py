import os
import csv
import time
from datetime import datetime
import subprocess


def is_internet_available():
    """Check internet connectivity by pinging Google's DNS"""
    try: 
        monitoring_test = subprocess.run(["ping", "-c", "10", "8.8.8.8"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{monitoring_test}")
        return True
    except Exception:
        return False
     
def log_disruption(start_time, end_time, filepath="connectivity_log.csv"):
    # Check if the file exists
    file_exists = os.path.isfile(filepath)

    with open(filepath, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            # Write headers if the file is new
            writer.writerow(["Start Interruption", "End Interruption"])
        writer.writerow([start_time, end_time])


def monitor_connectivity():
    print("Monitoring internet connectivity. Press CTRL+C to stop.")
    connection_down = False
    down_start_time = None

    while True: 
        if is_internet_available():
            if connection_down:
                # Connection restored: log the downtime
                down_end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Connection restored at {down_end_time}")
                log_disruption(down_start_time, down_end_time)
                connection_down = False
                down_start_time = None
        
        else:
            if not connection_down:
                # Connection lost; log the start time
                down_start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Connection lost at {down_start_time}")
                connection_down = True

        # Wait a few seconds for next check
        time.sleep(5)

if __name__ == "__main__":
    try:
        monitor_connectivity()
    except KeyboardInterrupt:
        print("\n Monitoring stopped.")
