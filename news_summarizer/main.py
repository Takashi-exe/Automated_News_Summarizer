import os
import smtplib # Module for email sending
# import schedule
from email.message import EmailMessage  # Import EmailMessage for email creation
from dotenv import load_dotenv  # Import load_dotenv for .env variables
from scraper import get_news, subject, text
from scheduler import schedule_job

# Load environment variables from .env file
load_dotenv()

EMAIL_SENDER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_RECIEVER = os.environ.get('EMAIL_RECIEVER')

# Create email message object
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_RECIEVER
msg.set_content(text)

def send_email():
    if text:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
    else:
        print(f"No articles found...\t")


def main():
    get_news()
    time_to_send = "15:54"
    schedule_job(time_to_send, send_email)

if __name__ == '__main__':
    main()
