import smtplib
import ssl
from email.message import EmailMessage
EMAIL= "sender email@gmail.com"
APP_PASSWORD= "your app password"
RECEIVER= "receiver email@gmail.com "
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "Hello sir...."
msg.set_content("The email was shared by VGU")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context = context) as server :
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)