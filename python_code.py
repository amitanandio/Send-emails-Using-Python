import smtplib
import getpass
from email.mime.text import MIMEText
def send_email():
    sender_address='coding.tmail@gmail.com'
    password=getpass.getpass()
    subject='My First Project on Sending Mail'
    msg='''
        Hello Everyone!
        i have conmpleted my first project on sending mail via python.
        i am feeling proud to share with you the pthon code
        Hope you will read it carefully
        
        Thank you!
        Amit Anand
        '''
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_address, password)
    msg=MIMEText(msg)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']='coding.tmail@gmail.com'
    recipients=['reciever mailid','another reciever emailid'] # you can send to multiple id also
    server.sendmail(sender_address, recipients, msg.as_string())
send_email()