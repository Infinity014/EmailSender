# Email Sender Made in Python.
# To Send email place the app password for you google account to the key_email Variable.
# Enter the email of tyour google account to emailSender.
# You can even try to implement the EmailValidator from the repository.
# Play around with the values as much as you like and have fun.
# Note : don't use for spamming or any un-ethical purpose.
from email.message import EmailMessage as eM
import ssl
import smtplib
from pwdEmailSender import key

key_email = key
emailSender = 'meghpatel9112@gmail.com'
emailReciver = input("Enter Email: ")

subject = input("Enter Subject: ")

bodyPrompt = input("Enter File Name: ")

try:
    f = open(bodyPrompt,'r')
except Exception as e:
    exit("Invalid file name given. Make sure that the file is in the same directory as the program file")
body = f.read()

em = eM()
em['From'] = emailSender
em['To'] = emailReciver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

co  = input(f'''**Send Email ?**
      
      To : {emailReciver}
      
      Subject : {subject}
      body : {bodyPrompt} 
      
      Enter [y]For yes and [n]For no: ''')

co = co.lower()

if co == 'n':
    exit('Email Not Sent')
elif co == 'y':

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(emailSender,key_email)
        smtp.sendmail(emailSender,emailReciver,em.as_string())
    exit("Email Sent")
else: 
    exit("Please Enter a Valid Option")