import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")

message = """\
    Subject: Welcome Ubaydah

    課題内容です。
"""

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, "lakt127@gmail.com", message)
