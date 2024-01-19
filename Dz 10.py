import sqlite3
import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://sinoptik.ua/погода-рим"
r = requests.get(URL_TEMPLATE)

html = bs(r.text, "html.paser")

min = html.find_all('div', class_='min')
n = 0
min_ = []
for i in min:
    min_.append([ int(span.text.replace('°', ''))])
    n += 1

connection = sqlite3.connect('temp.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE weather(id INT PRIMARY KEY, date INT, temp INT)""")
cursor.execute("""INSERT INTO weather(min) VALUES(?,?), (?,?), 
(?,?), (?,?), (?,?)""" , min_)

cursor.execute("""SELECT * FROM weather""")
print(cursor.fetchall())
connection.commit()
connection.close()