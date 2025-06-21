# 🧠 Attendance Analyzer Agent

An **Agentic AI System** that autonomously analyzes daily attendance data, classifies students as **Present**, **Absent**, **Late**, or **On Leave**, and generates structured reports — with **zero human intervention**.

Built with Python, Streamlit, and Pandas.

---

## ⚙️ Features

- ✅ **Autonomous AI Agent**
- 📊 Structured attendance classification
- 🔍 Late/Absent/Leave detection based on check-in time
- 📅 Daily automated processing
- 📑 Visual and textual summary reports
- 📬 Email reporting system
- 🌐 Streamlit dashboard for insights

---

## 📁 Project Structure

Attendance_Analyzer_Agent/
│
├── agents/ # All autonomous agents
│ ├── analyzer_agent.py # Classifies raw attendance data
│ ├── daily_planner.py # Orchestrates the full workflow daily
│ ├── reporter_agent.py # Generates and emails daily report
│ └── send_email.py # Handles email dispatch
│
├── data/
│ ├── raw/ # Input CSV files
│ │ └── raw_attendance.csv
│ └── processed/ # Output structured attendance
│ └── structured_attendance_with_status.csv
│
├── reports/ # Daily summary reports (text)
│
├── last_processed.txt # Tracks last processed date
├── dashboard.py # Streamlit dashboard UI
├── requirements.txt # All Python dependencies
└── README.md # You're here

yaml
Copy code

---

## 🔧 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/attendance-analyzer-agent.git
cd attendance-analyzer-agent
2. Create Virtual Environment
bash
Copy code
python -m venv .venv
3. Activate Virtual Environment
Windows:

bash
Copy code
.venv\Scripts\activate
Linux/macOS:

bash
Copy code
source .venv/bin/activate
4. Install Requirements
bash
Copy code
pip install -r requirements.txt
🚀 Usage
➤ 1. Place your attendance input
Put your raw file here:

bash
Copy code
data/raw/raw_attendance.csv
Ensure columns like:

c
Copy code
StudentID, Name, CheckInTime, Status
➤ 2. Run Main Agent
bash
Copy code
python agents/daily_planner.py
This agent:

Detects new data

Runs classification

Generates report

Emails results

Runs forever like a bot 👇

arduino
Copy code
✅ Attendance processed and saved
🔄 Daily Planner Agent running... (CTRL+C to stop)
➤ 3. Open Dashboard (optional)
bash
Copy code
streamlit run dashboard.py
Then open:
http://localhost:8501

➤ 4. Manually Trigger Report (Optional)
bash
Copy code
python agents/reporter_agent.py
📬 Email Automation
To enable Gmail sending:

Go to: https://myaccount.google.com/apppasswords

Generate an app password

Replace the fields inside send_email.py:

python
Copy code
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_generated_app_password"
🧠 What Makes It Agentic AI?
This system fulfills all criteria:

Agentic Capability	✅ Implemented
Autonomous Decision Making	✅
Planning & Execution Loop	✅
Perception from Data	✅
Action (classify, report, email)	✅
Optional UI	✅

🛠 Built With
Python

Pandas

Streamlit

Matplotlib

SMTP Email

🧑‍💻 Author
Nishant Kumar Singh
🧠 MERN Stack & AI Developer
🎓 Galgotias University
📬 Email: your_email@gmail.com
🔗 LinkedIn | GitHub

💡 Future Improvements
Add LLM agent to generate natural-language insights

Use CrewAI / LangChain for multi-agent behavior

Connect to biometric/RFID systems

Store long-term insights for predictive attendance

🏁 Final Notes
This project is fully autonomous, agent-driven, and built for real-world use.