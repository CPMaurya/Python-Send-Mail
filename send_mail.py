import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass


# username = "sender@gmail.com"
# password = "1234@asdf"

def send_mail(text="body", subject="hello", to_emails=None, html=None):
    assert isinstance(to_emails, list)
    username = input("Enter Sender Mail ID (ex:- sender@gmail.com): ")
    password = getpass("Enter your valid password: ")

    from_email='User <' + username + '>'

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject

    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)

    if html is not None:
        html_part = MIMEText(html, 'html')
        msg.attach(html_part)

    msg_str = msg.as_string()
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
