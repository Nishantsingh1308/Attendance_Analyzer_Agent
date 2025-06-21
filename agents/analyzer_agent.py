# analyzer_agent.py
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.classify_attendance import classify_attendance


def run_attendance_analysis(input_path, output_path):
    if not os.path.exists(input_path):
        print("❌ Raw attendance file not found.")
        return

    print("✅ Analyzer Agent started...")

    # Load the raw dataset
    df = pd.read_csv(input_path)

    # Apply classification using your function
    df["Attendance Status"] = df.apply(classify_attendance, axis=1)

    # Save output
    df.to_csv(output_path, index=False)
    print(f"✅ Attendance analyzed and saved to: {output_path}")

# Sample usage (can be triggered by main.py)
if __name__ == "__main__":
    run_attendance_analysis(
        input_path="data/raw/rich_attendance_dataset.csv",
        output_path="data/processed/structured_attendance_with_status.csv"
    )
