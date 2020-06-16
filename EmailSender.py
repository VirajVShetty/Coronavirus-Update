#!/usr/bin/python
""" Authors - Akshay Sonawane and Viraj Shetty """

import smtplib
from Corona_Updates import update

sender = 'corona.updates.av.2020@gmail.com'
receivers = ['akshaysonawane10526@gmail.com', 'virajshetty1@hotmail.com']
pwd = 'sakecboys-akvi'


if __name__ == "__main__":

    india_list, india_percent, maha_list, maha_percent = update()

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: Coronavirus Cases Update

    Current Active Cases     
        India :- {}             
        Maharasgtra :- {}       
        Mumbai :- {}   

    People Recovered:
        India :- {}             
        Maharasgtra :- {}       
        Mumbai :- {} 

    Death in india: {}
    Total Recovery Percentage: {}%

    """.format(india_list[0], maha_list[0], "work in progress", india_list[1], maha_list[1], "Work in progress",india_list[2], india_percent)

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receivers, message)
        print("Successfully sent email")
        smtpObj.quit()
    except smtplib.SMTPException:
        print("Error: unable to send email")
