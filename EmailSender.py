#!/usr/bin/python
""" Authors - Akshay Sonawane and Viraj Shetty """

import smtplib

sender = 'corona.updates.av.2020@gmail.com'
receivers = ['123akshaysonawane@gmail.com']
pwd = 'sakecboys-akvi'

message = """From: From Your Daily Coronavirus Updater <from@fromdomain.com>
Subject: Coronavirus Cases Update

<h1>Current Active Cases<h1>        
    India :- {}             
    Maharasgtra :- {}       
    Mumbai :- {}   

People Recovered:
    India :- {}             
    Maharasgtra :- {}       
    Mumbai :- {} 

Total Recovery Percentage: {}%

""".format("6969","654","63738","6969","654","63738", "99")

if __name__ == "__main__":
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error: unable to send email")
