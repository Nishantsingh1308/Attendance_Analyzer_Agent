# dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- CONFIG ---
FILE_PATH = "data/processed/structured_attendance_with_status.csv"

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Attendance Analyzer Dashboard",
    layout="centered"
)

st.title("📊 Attendance Analyzer Dashboard")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    if not os.path.exists(FILE_PATH):
        return None
    return pd.read_csv(FILE_PATH)

df = load_data()

if df is None:
    st.warning("⚠️ No attendance data found. Make sure the file exists at:")
    st.code(FILE_PATH)
else:
    # --- SUMMARY STATS ---
    st.subheader("🧾 Attendance Summary")
    total = len(df)
    status_counts = df['Attendance Status'].value_counts().to_dict()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Students", total)
    with col2:
        st.write("### Status Breakdown")
        for status in ["Present", "Late", "Absent", "On Leave"]:
            st.markdown(f"- **{status}**: {status_counts.get(status, 0)}")

    # --- PIE CHART ---
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
    ax.pie(sizes, labels=labels, colors=[colors[s] for s in labels],
           autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    st.pyplot(fig)

    # --- RAW DATA TABLE ---
    with st.expander("📋 View Full Attendance Table"):
        st.dataframe(df, use_container_width=True)
