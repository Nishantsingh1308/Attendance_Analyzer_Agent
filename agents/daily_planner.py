# agents/planner_agent.py

import os
import time
import schedule
from datetime import datetime
from analyzer_agent import run_attendance_analysis

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"
PROCESSED_LOG = "last_processed.txt"

def get_latest_file(folder):
    files = [f for f in os.listdir(folder) if f.endswith(".csv")]
    if not files:
        return None
    files = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
    return os.path.join(folder, files[0])

def already_processed(file_path):
    if not os.path.exists(PROCESSED_LOG):
        return False
    with open(PROCESSED_LOG, 'r') as f:
        last = f.read().strip()
        return last == file_path

def mark_as_processed(file_path):
    with open(PROCESSED_LOG, 'w') as f:
        f.write(file_path)

def run_planner():
    print(f"\n🧠 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Planner Agent started...")

    latest_file = get_latest_file(RAW_FOLDER)
    if not latest_file:
        print("📂 No raw CSV file found.")
        return

    if already_processed(latest_file):
        print("⏳ No new file to process.")
        return

    print(f"📄 New file detected: {latest_file}")
    output_file = os.path.join(PROCESSED_FOLDER, "structured_attendance_with_status.csv")
    run_attendance_analysis(latest_file, output_file)
    mark_as_processed(latest_file)
    print("✅ Processing complete!")

# Schedule the agent to run daily at 10:00 AM
schedule.every().day.at("10:00").do(run_planner)

# Loop forever
if __name__ == "__main__":
    print("🔄 Daily Planner Agent running... (CTRL+C to stop)")
    while True:
        schedule.run_pending()
        time.sleep(30)
