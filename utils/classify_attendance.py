import pandas as pd
from datetime import datetime

# === Load the rich attendance dataset ===
input_file = "data/raw/rich_attendance_dataset.csv"  # Adjust path as needed
df = pd.read_csv(input_file)

# === Function to classify each person's attendance status ===
def classify_attendance(row):
    time_in = row['Time In']
    leave_type = str(row['Leave Type']).strip()

    # Handle blank or missing Time In
    if pd.isna(time_in) or time_in.strip() == "":
        return "On Leave" if leave_type else "Absent"

    try:
        time_obj = datetime.strptime(time_in.strip(), "%H:%M")
    except ValueError:
        return "Invalid Time"

    if time_obj < datetime.strptime("10:00", "%H:%M"):
        return "Present"
    elif time_obj <= datetime.strptime("11:00", "%H:%M"):
        return "Late"
    else:
        return "Absent"

# === Apply the function to the dataset ===
df["Attendance Status"] = df.apply(classify_attendance, axis=1)

# === Save the structured dataset with status ===
output_file = "data/processed/structured_attendance_with_status.csv"
df.to_csv(output_file, index=False)

print("✅ Attendance processed and saved to:", output_file)
