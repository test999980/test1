import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header
from email import charset
from email.utils import formatdate
import os

port = 465
smtp_server = "smtp.gmail.com"
USER_EMAIL = os.environ.get("USER_EMAIL")
USER_PASSWORD = os.environ.get("USER_PASSWORD")
TO_MAIL = os.environ.get("TO_MAIL")
MAIL_TITLE = os.environ.get("MAIL_TITLE")
MAIL_BODY = os.environ.get("MAIL_BODY")
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

subject = MAIL_TITLE
bodyText = MAIL_BODY

# SMTPサーバに接続
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.starttls()
smtpobj.login(USER_EMAIL, USER_PASSWORD)

# メール作成
msg = MIMEText(bodyText)
msg['Subject'] = subject
msg['From'] = USER_EMAIL
msg['To'] = TO_MAIL
msg['Date'] = formatdate()

# 作成したメールを送信
smtpobj.send_message(msg)
smtpobj.close()
