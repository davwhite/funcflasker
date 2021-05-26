import requests 
from bs4 import BeautifulSoup 

def get_rates():
    URL = "https://www.x-rates.com/table/?from=USD&amount=1"
    r = requests.get(URL) 

    soup = BeautifulSoup(r.content, 'html.parser') 
    ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")
    rates = []
    for tableVal in ratelist:
        trList = tableVal.findAll('tr')
        for trVal in trList[:6]:
            rates.append(trVal.text)
    return str(rates)