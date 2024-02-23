import os
import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import date
import scanner

PORT = 587
EMAIL_SERVER = 'smtp-mail.outlook.com'
today = date.today()
d1 = today.strftime("%d.%m.%Y")

envars = r'C:\Users\ishan\Desktop\Ishan\Coding\Projects\BabaStocks\BabaStocksScanners\.env'
load_dotenv(envars)

sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_emails, name):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = f'The Yoga of TA <{sender_email}>'
    msg['To'] = ', '.join(receiver_emails)

    text_content = MIMEText(f"""\
        Hi {name},
        Please find your stock recommendations from "THE YOGA OF TA" for the date "{d1}".
        
        Volume breakout along with moving average crossover and bounce For Cash:
        {scanner.stock_list_cash_screener_string}

        Volume breakout along with moving average crossover and bounce For Nifty 50:
        {scanner.stock_list_nifty_50_screener_string}

        Volume breakout along with moving average crossover and bounce For Nifty 100:
        {scanner.stock_list_nifty_100_screener_string}

        Volume breakout along with moving average crossover and bounce For Nifty 200:
        {scanner.stock_list_nifty_200_screener_string}

        Volume breakout along with moving average crossover and bounce For Nifty 500:
        {scanner.stock_list_nifty_500_screener_string}
        
        Volume breakout along with moving average crossover and bounce For Midcap 50:
        {scanner.stock_list_midcap_50_screener_string}
        

        Best regards,
        THE YOGA OF TA TEAM
    """)

    msg.attach(text_content)  # Attach the text content to the email message

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
        receiver_emails=['yateenjoshi@gmail.com', 'ishanprivate14@gmail.com', 'suruchigtm@gmail.com', 'prafulla.huddar@gmail.com', 'divatema@gmail.com', 'aru.3412@gmail.com'],
    )
    print("After")
