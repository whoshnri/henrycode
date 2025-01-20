import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = 'smtp.gmail.com'


sender_email = 'henrybassey2007@gmail.com'
password_email = ''
from datetime import *
now_time = datetime.now().strftime('%H:%M:%S') #current time
now_date = date.today() #current date


body =  f'''
Hey there this is test email for my study
It took me all day to get this to work 
im so happy....
Now ill pperfect this skill in python and then ill learn how to send html type emails with nico looking features
Emial sent on {now_date} at {now_time}
        '''



def emailer(subject, reciever_email):
    msg = MIMEText(body , 'plain')
    msg['Subject'] = subject
    msg['From'] = formataddr(('Python Test', f'{sender_email}'))
    msg['To'] = reciever_email
    msg['BCC'] = sender_email

    try:
        with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
            server.starttls()
            server.debuglevel(1)
            server.login(sender_email, password_email)
            server.sendmail(sender_email,reciever_email,msg.as_string())
            print('Email sent successfully')
    except smtplib.SMTPServerDisconnected as e:
        print(f'Error : {e}')
    except Exception as e :
        print(f'An Error Occured: {e}')


emails = ('henrybassey2007@gmail.com' , 'horacedaphne@gmail.com' , 'henrybassey2007@outlook.com', 'henrybassey2007@yahoo.com')

if __name__ == '__main__':
    #for sending to multiple people
    count = 0
    for email in emails:
        emailer(f"Batch Email {now_date}" , email)
        print(f'Email count: {emails.index(email) + 1}')
    








