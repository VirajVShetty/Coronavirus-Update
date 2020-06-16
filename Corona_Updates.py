"""
    Authors:

    Viraj Shetty
    Akshay Sonawane
    
"""
def update():
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
    """
    print("Corona Updates")
    print("---------------------")
    print("India")
    print(" ")
    print("Active: "+stat[0])
    print("Cured: "+stat[1])
    print("Deaths: "+stat[2])
    print("Migrated: "+stat[3])
    """
    i_p = (int(stat[1])*100/int(int(stat[0])+int(stat[1]))))

    state = []
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(3)')
    y = re.findall(r'\d+',str(x[0]))
    state.append(int(y[0]))
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(4)')
    y = re.findall(r'\d+',str(x[0]))
    state.append(int(y[0]))
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(5)')
    y = re.findall(r'\d+',str(x[0]))
    state.append(int(y[0]))
    x = soup.select('.table > tbody:nth-child(2) > tr:nth-child(20) > td:nth-child(6)')
    y = re.findall(r'\d+',str(x[0]))
    state.append(int(y[0]))
    """
    print("---------------------")
    print("Maharashtra")
    print(" ")
    print("Active: "+str(state[0]))
    print("Cured: "+str(state[1]))
    print("Deaths: "+str(state[2]))
    print("Total: "+str(state[3]))
    """
    m_p = (int(state[1])*100/int(state[3])))
    return stat[0],stat[1],stat[2],stat[3],i_p,state[0],state[1],state[2],state[3],m_p
