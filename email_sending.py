import smtplib, ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
TO_MAIL = os.environ.get("TO_MAIL")

message = """\
    ${{ github.event.issue.title }}
    ${{ github.event.issue.body }}
"""

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.sendmail(USER_EMAIL, TO_MAIL, message)
