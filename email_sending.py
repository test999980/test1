import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header
from email import charset
import os

port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
TO_MAIL = os.environ.get("TO_MAIL")
MAIL_TITLE = os.environ.get("MAIL_TITLE")
MAIL_BODY = os.environ.get("MAIL_BODY")

cset = 'utf-8'

message = MIMEText(u'日本語のメールだよ★', 'plain', cset)
message['Subject'] = Header(u'メール送信テスト', cset)
msg['From'] = {USER_EMAIL}
msg['To'] = {TO_MAIL}
msg['Date'] = formatdate()

context = ssl.create_default_context()

server = smtplib.SMTP_SSL(smtp_server, port, context=context)

server.login(USER_EMAIL, USER_PASSWORD)
server.send_message(message)
