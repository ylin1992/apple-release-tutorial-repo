import ssl
import smtplib
import os
from config import SENDER_EMAIL, SENDER_PWD, SSL_PORT
from config import RECEIVER_EMAIL

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

if __name__ == '__main__':
    email = SSLEmail(sender=SENDER_EMAIL, receiver=RECEIVER_EMAIL, subject="test subject", content="test contentgit a")
    email.send_email()