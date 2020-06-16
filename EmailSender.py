#!/usr/bin/python
""" Authors - Akshay Sonawane and Viraj Shetty """

import smtplib

sender = 'corona.updates.av.2020@gmail.com'
receivers = ['akshaysonawane10526@gmail.com', 'virajshetty1@hotmail.com']
pwd = 'sakecboys-akvi'


message = """From: From Your Daily Coronavirus Updater <from@fromdomain.com>
Subject: Coronavirus Cases Update

Current Active Cases     
    India :- {}             
    Maharasgtra :- {}       
    Mumbai :- {}   

People Recovered:
    India :- {}             
    Maharasgtra :- {}       
    Mumbai :- {} 

Total Recovery Percentage: {}%

""".format("6969","654","Will update soon","6969","654","63738", "Will update soon")

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
