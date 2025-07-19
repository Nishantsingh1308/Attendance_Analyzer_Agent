import smtplib
from email.message import EmailMessage
from datetime import datetime
import os

# CONFIGURE THESE
EMAIL_SENDER = "myshant150@gmail.com"
EMAIL_PASSWORD = "hjqz trdi vton apzs"
EMAIL_RECEIVER = "aayushichaudhary530602@gmail.com"

def send_attendance_email():
    today = datetime.today().strftime('%Y%m%d')
    report_path = f"reports/attendance_report_{today}.txt"
    chart_path = f"reports/attendance_chart_{today}.png"

    if not os.path.exists(report_path) or not os.path.exists(chart_path):
        print("❌ Report or chart file missing.")
        return

    msg = EmailMessage()
    msg['Subject'] = f"📊 Attendance Report – {datetime.today().strftime('%Y-%m-%d')}"
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg.set_content("Attached are today's attendance summary and pie chart.")

    # Attach text file
    with open(report_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=os.path.basename(report_path))

    # Attach chart image
    with open(chart_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='image', subtype='png', filename=os.path.basename(chart_path))

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("✅ Attendance email sent successfully.")

# Run as script
if __name__ == "__main__":
    send_attendance_email()
