import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://bank.gov.ua/ua/markets/exchangerates/"
r = requests.get(URL_TEMPLATE)

html = bs(r.text, "html.paser")

data = html.find_all('td')
u = 0
for i in data:
    if 'Долар США' in i:
        u = float(data[data.indez(i) + 1].text.replace(',','.'))

def convertor():
    g = float(input('What you what to convert?'))
    print(g/u)

convertor()

import sqlite3