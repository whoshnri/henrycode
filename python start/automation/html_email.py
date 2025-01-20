#html emails

import smtplib
from datetime import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

SERVER = 'smtp.gmail.com'
PORT = 587


name_person = ''
email_sender = 'henrybassey2007@gmail.com'
password = ''

message_body = f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test E-mail</title>
    <style type="text/css">
        h2{{
            margin : auto;
            width: 100%;
            font-family: Arial, Helvetica, sans-serif;
        }}
        p{{
            font-family: Arial, Helvetica, sans-serif;
            width: 100%;
            margin: auto
        }}
        button{{
            text-align: center;
            margin: auto;
            color: white;
            background-color: #2f2f2f;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <h2>Hello,{name_person}</h2>
    <p>You have been cordially invited to the wedding of <b>Mr and Mrs Smith.</b><br>Do well to attend the ceremony</p>
    <p>Click the button below to print your e-ticket</p>
    <button><a href="http://www.google.com"></a>Get Invitation Card</button>
    <p><a href="terms.jhsjh">Terms Apply <br>Read More</a></p>
</body>
</html>

"""


def emailer(email_reciever , name_person):
    msg = MIMEMultipart()
    msg['FROM'] = formataddr(("Invitation" , email_sender))
    msg['TO'] = email_reciever
    msg['Subject'] = 'Wedding Invitation'
    msg['BCC'] = email_sender

    msg.attach(MIMEText(message_body , 'html'))

    try:
        with smtplib.SMTP(SERVER , PORT) as server:
            server.starttls()
            server.login(email_sender , password)
            server.sendmail(email_sender , email_reciever , msg.as_string())

            print('Mail sent successfully')
    except smtplib.SMTPServerDisconnected as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An error occured: {e}')


if __name__ == '__main__' :
    emailer('horacedaphne@gmail.com','Horace Daphne')