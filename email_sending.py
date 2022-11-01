import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
TO_MAIL = os.environ.get("TO_MAIL")
MAIL_TITLE = os.environ.get("MAIL_TITLE")
MAIL_BODY = os.environ.get("MAIL_BODY")


message = f"""\
    Subject: {MAIL_TITLE}
    
    {MAIL_BODY}
"""

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, TO_MAIL, message)
