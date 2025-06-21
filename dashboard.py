# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# File path (you can allow user to pick different files later)
FILE_PATH = "data/processed/structured_attendance_with_status.csv"

# Load Data
@st.cache_data
def load_data():
    if not os.path.exists(FILE_PATH):
        return None
    return pd.read_csv(FILE_PATH)

df = load_data()

st.set_page_config(page_title="Attendance Dashboard", layout="centered")
st.title("📊 Attendance Analyzer Dashboard")

if df is None:
    st.error("No processed attendance file found.")
else:
    # Stats
    st.subheader("🧮 Summary")
    total = len(df)
    status_counts = df['Attendance Status'].value_counts().to_dict()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Students", total)
    with col2:
        for status in ["Present", "Late", "Absent", "On Leave"]:
            st.write(f"**{status}**: {status_counts.get(status, 0)}")

    # Pie Chart
    st.subheader("📈 Attendance Pie Chart")
    labels = []
    sizes = []
    colors = {
        "Present": "#4CAF50",
        "Late": "#FFC107",
        "Absent": "#F44336",
        "On Leave": "#2196F3"
    }

    for status in ["Present", "Late", "Absent", "On Leave"]:
        count = status_counts.get(status, 0)
        if count > 0:
            labels.append(status)
            sizes.append(count)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=[colors[s] for s in labels], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    # Raw Data
    with st.expander("📋 View Full Attendance Table"):
        st.dataframe(df)

