#!/usr/bin/python
""" Authors - Akshay Sonawane and Viraj Shetty """

import smtplib

sender = 'corona.updates.av.2020@gmail.com'
receivers = ['akshay.sonawane@sakec.ac.in']

message = """From: From Your Daily Coronavirus Updater <from@fromdomain.com>
Subject: Coronavirus Cases Update

This is a test e-mail message.
"""

if __name__ == "__main__":
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login('corona.updates.av.2020', 'sakecboys-akvi')
        smtpObj.sendmail(sender, receivers, message)
        print
        "Successfully sent email"
    except smtplib.SMTPException:
        print
        "Error: unable to send email"
