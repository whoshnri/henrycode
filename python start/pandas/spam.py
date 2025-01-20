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
org = ''

body =  f'''
Dear {org} Support Team,  

I hope this message finds you well. My name is [Your Name], and I am deeply passionate about learning and personal development. I am particularly interested in [specific topic/course of interest] offered on your platform.  

As a student [or mention your current status, e.g., "aspiring data analyst"], I am seeking opportunities to enhance my skills but currently have limited financial resources. I was wondering if Coursera offers any free access programs or scholarships that I could apply for to pursue this course.  

I would be immensely grateful for any guidance or support you can provide. Thank you for your time and consideration.  

Looking forward to your response.  

Best regards,  
Henry Bassey 




Just in case you wanna reach out, 
Whatsapp: +234 913 179 5757
@xyz_07hb on Instagram  

        '''



def emailer(reciever_email , company):
    global org
    org = company
    msg = MIMEText(body , 'plain')
    msg['Subject'] = 'Request for Access to Free Course Opportunity'
    msg['From'] = formataddr(('Requests for Courses', f'{sender_email}'))
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


emails = []
names = []

if __name__ == '__main__':
    #for sending to multiple people
    count = 0
    for email in emails:
        emailer(email , names(emails.index(email)))
        print(f'Email count: {emails.index(email) + 1}')

    








