from curl_cffi import requests
import smtplib
from email.message import EmailMessage
import datetime
import os
import re

def check_tickets():
    api_url = "https://sscnapoli.ticketone.it/api/event"
    catalog_url = "https://sscnapoli.ticketone.it/catalog"

    try:
        response = requests.get(api_url, impersonate="chrome")

        if response.status_code == 403:
            print(f"[{datetime.datetime.now()}] Still blocked by firewall (403).")
            return

        if re.search(r'\b(milan|ac|mailand)\b', response.text, re.IGNORECASE):
            send_email(catalog_url)
            print(f"[{datetime.datetime.now()}] MILAN/AC found! Email sent.")
        else:
            print(f"[{datetime.datetime.now()}] Match not found.")

    except Exception as e:
        print(f"[{datetime.datetime.now()}] Error: {e}")

def _required_env(name):
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

def send_email(url):
    sender = _required_env("EMAIL_USER")
    password = _required_env("EMAIL_PASS")
    receiver = _required_env("EMAIL_TO")

    msg = EmailMessage()
    msg.set_content(f'The AC Milan match was detected!\n\nGo buy them now at: {url}')
    msg['Subject'] = 'MILAN Tickets Found!'
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    check_tickets()