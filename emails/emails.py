import ssl
import smtplib
import os
from config import SENDER_EMAIL, SENDER_PWD, SSL_PORT
<<<<<<< HEAD
from config import RECEIVER_EMAIL, SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
=======
from config import RECEIVER_EMAIL
>>>>>>> 89ab16174b95abe62fe4a44c94bf04c65d73d005

class Email:
    sender = None
    receiver = None
    subject = None
    content = None

    def __init__(self, sender, receiver, subject="", content=""):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.content = content

    def set_email(self, **kwargs):
        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])
            else:
                raise ValueError('"%s" is not defined'%k) 

    def get_email_info(self):
        return self.__repr__()

    def send_email(self):
        return NotImplemented

    def __repr__(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'subject': self.subject,
            'content': self.content
        }

class SSLEmail(Email):

    def send_email(self):
        context = ssl.create_default_context()
        message = """\
        Subject: %s!

        %s."""%(self.subject, self.content)

        with smtplib.SMTP_SSL("smtp.gmail.com", SSL_PORT, context=context) as server:
            server.login(self.sender, SENDER_PWD)
            server.sendmail(self.sender, self.receiver, message)

<<<<<<< HEAD
class SendGridEmail(Email):
    def send_email(self):
        message = Mail(
        from_email=self.sender,
        to_emails=self.receiver,
        subject=self.subject,
        html_content=self.content)
        try:
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.body)

if __name__ == '__main__':
    email = SendGridEmail(sender=SENDER_EMAIL, receiver=RECEIVER_EMAIL, subject="test subject", content="test contentgit a")
=======
if __name__ == '__main__':
    email = SSLEmail(sender=SENDER_EMAIL, receiver=RECEIVER_EMAIL, subject="test subject", content="test contentgit a")
>>>>>>> 89ab16174b95abe62fe4a44c94bf04c65d73d005
    email.send_email()