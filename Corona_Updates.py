""" Authors - Akshay Sonawane and Viraj Shetty """
import urllib
import urllib.request, urllib.parse
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "https://www.mohfw.gov.in/"

html = urllib.request.urlopen(url, context=ctx).read()

soup = BeautifulSoup(html,'html.parser')

tags = soup.findAll('strong')

stats = []

for tag in tags:
    x = tag.get_text()
    if x.isnumeric():
        if x not in stats:
            stats.append(x)
stat = stats[:4]
print("Corona Updates")
print("Active: "+stat[0])
print("Cured: "+stat[1])
print("Deaths: "+stat[2])
print("Migrated: "+stat[3])
