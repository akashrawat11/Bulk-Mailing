import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')


    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('Senders E-mail','password')
    try:
        server.sendmail('Senders E-mail','recievers E-mail','Subject: {}\n\n Message <python>'.format("Subject"))
    except:
        print("not able to send")
server.quit()
