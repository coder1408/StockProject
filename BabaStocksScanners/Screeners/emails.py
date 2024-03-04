import os
import smtplib
import ssl  # Add this line for ssl module
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from datetime import date

PORT = 587
EMAIL_SERVER = 'smtp-mail.outlook.com'
today = date.today()
d1 = today.strftime("%d-%m-%Y")

envars = r'StockProject\BabaStocksScanners\.env'
load_dotenv(envars)

sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_emails, name, attachment_path):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = f'The Yoga of TA <{sender_email}>'
    msg['To'] = ', '.join(receiver_emails)

    text_content = MIMEText(f"""\
        Hi {name},
        Please find your stock screener requirements from "THE YOGA OF TA" for the date "{d1}".
        
        Best regards,
        THE YOGA OF TA TEAM
    """)
    msg.attach(text_content)  # Attach the text content to the email message

    # Attach the file
    attachment = open(attachment_path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
    msg.attach(part)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server
    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls(context=context)
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_emails, msg.as_string())

if __name__ == "__main__":
    print("Before")
    send_email(
        subject="Today's Stock Recommendations",
        name="Yateen",
        receiver_emails=['yateenjoshi@gmail.com', 'ishanprivate14@gmail.com'],
        attachment_path=rf"C:\Users\ishan\Downloads\PortfolioAnalysisPaid\PortfolioAnalysis{d1}.xlsx",  # Replace with the actual path to your file
    )
    print("After")
