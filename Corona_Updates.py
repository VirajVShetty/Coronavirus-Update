"""
    Authors:

    Viraj Shetty
    Akshay Sonawane
    
"""
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.mohfw.gov.in/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup.findAll('strong')

stats = []
state = []

def update():
    """
    This Function does web-scraping from website "https://www.mohfw.gov.in/" and gives corona update.
    :return: case in india, recovery percentage of india, case in maharashtra, recovery percentage of maharashtra
    """
    for tag in tags:
        x = tag.get_text()
        if x.isnumeric():
            if x not in stats:
                stats.append(x)

    stat = stats[:4]
    i_p = (int(stat[1]) * 100 / int(int(stat[0]) + int(stat[1])))

    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(3)')
    y = re.findall(r'\d+', str(x[0]))
    state.append(int(y[0]))
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(4)')
    y = re.findall(r'\d+', str(x[0]))
    state.append(int(y[0]))
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(5)')
    y = re.findall(r'\d+', str(x[0]))
    state.append(int(y[0]))
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(6)')
    y = re.findall(r'\d+', str(x[0]))
    state.append(int(y[0]))

    m_p = (int(state[1]) * 100 / int(state[3]))
    return stat, i_p, state, m_p

