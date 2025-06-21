# agents/reporter_agent.py

import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

# Paths
PROCESSED_FILE = "data/processed/structured_attendance_with_status.csv"
REPORT_FOLDER = "reports"

def generate_attendance_report():
    if not os.path.exists(PROCESSED_FILE):
        print("❌ Processed attendance file not found.")
        return

    df = pd.read_csv(PROCESSED_FILE)
    status_counts = df['Attendance Status'].value_counts().to_dict()
    total = len(df)

    # Text Report
    report_lines = [
        f"📅 Attendance Summary for {datetime.today().strftime('%Y-%m-%d')}",
        f"Total Students: {total}",
        "-" * 30,
    ]

    for status in ["Present", "Late", "Absent", "On Leave"]:
        count = status_counts.get(status, 0)
        report_lines.append(f"{status:<10}: {count}")

    report = "\n".join(report_lines)
    print(report)

    # Ensure report folder
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

    # Save text report
    report_file = f"{REPORT_FOLDER}/attendance_report_{datetime.today().strftime('%Y%m%d')}.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n✅ Report saved to {report_file}")

    # 🎨 Pie Chart
    labels = []
    sizes = []
    colors = {
        "Present": "#4CAF50",     # Green
        "Late": "#FFC107",        # Amber
        "Absent": "#F44336",      # Red
        "On Leave": "#2196F3"     # Blue
    }

    for status in ["Present", "Late", "Absent", "On Leave"]:
        count = status_counts.get(status, 0)
        if count > 0:
            labels.append(status)
            sizes.append(count)

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=[colors[s] for s in labels], autopct='%1.1f%%', startangle=90)
    plt.title("Attendance Distribution")
    plt.axis('equal')

    chart_file = f"{REPORT_FOLDER}/attendance_chart_{datetime.today().strftime('%Y%m%d')}.png"
    plt.savefig(chart_file)
    plt.close()

    print(f"📊 Pie chart saved to {chart_file}")

# Run if script is executed directly
if __name__ == "__main__":
    generate_attendance_report()
