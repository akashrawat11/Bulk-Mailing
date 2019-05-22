import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('ar053731@gmail.com','@123rawat')
    try:
        server.sendmail('ar053731@gmail.com','rawatakash9690@gmail.com','Subject: {}\n\n This is just a mail<python>'.format("python lib"))
    except:
        print("not able to send")
server.quit()