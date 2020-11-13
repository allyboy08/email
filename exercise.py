import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#https://myaccount.google.com/lesssecureapps


sender='alexsassman65@gmail.com'
receiver= ['leesterhorne8@gmail.com', "zengel1706@gmail.com"]
password= input("enter password: ")
subject="cool beans"
msg= MIMEMultipart()
msg['from']= sender
msg['to']= ", ".join(receiver)
msg['subject']= subject
body= "hi\n"
body= body + "hello"
msg.attach(MIMEText(body, 'plain'))
text= msg.as_string()
s= smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender,password)
#message= "hi"
#message= message + "hello"

s.sendmail(sender, receiver, text)
s.quit()
