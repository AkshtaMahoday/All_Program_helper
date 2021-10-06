import smtplib

import config


def send_email(subject, msg):
    try:
        rec_email = ['techysushrut@gmail.com','sukritji@gmail.com']
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, rec_email, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Hey!"
msg = "Hello there, how are you today?"

send_email(subject, msg)


-------------------------------------------------------



import smtplib

smtp_object=smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
import getpass
email= getpass.getpass("email:ff@gmail.com")
password= getpass.getpass("password:")
smtp_object.login(email,password)
from_adress= "abcd@gmail.com"
to_adress= input("who are u mailing?   ")
subject= input("enter subject line:  ")
message= input ("write message:   ")
msg= "subject: "+subject+'\n'+message
smtp_object.sendmail(from_adress,to_adress,msg)
