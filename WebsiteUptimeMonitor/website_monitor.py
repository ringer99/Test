import requests
import time
import smtplib

# UptimeRobot API Key
API_KEY = 'YOUR_UPTIMEROBOT_API_KEY'

# List of websites to monitor
websites = [
    {'name': 'Example', 'url': 'https://example.com'},
    {'name': 'Google', 'url': 'https://google.com'},
    {'name': 'Jumia', 'url': 'https://www.jumia.co.ke/'},
]

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS'
EMAIL_PASSWORD = 'YOUR_EMAIL_PASSWORD'
RECIPIENT_ADDRESS = 'RECIPIENT_EMAIL_ADDRESS'

