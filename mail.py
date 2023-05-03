import smtplib
import os 
from email.mime.text import MIMEText
async def send_email(message):
    sender = "olaaverina012@gmail.com"
    password = "hxkbfzwklegqorof"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    try:
        server.login(sender,password)
        msg = MIMEText(message)
        msg["Subject"] = "Новая заявка"
        await server.sendmail(sender,sender, msg.as_string())
        
    except Exception as _ex:
        print("Check login or password")

#if __name__ == "__main__":
    #send_email("dfgsrgre ertrete")