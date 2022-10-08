from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = requests.get(start_url)
soup = bs(browser.text,'html.parser')

star_table = soup.find_all('table')
temp_list = []
table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
radius = []
mass = []
distance = []

for i in range(1,len(temp_list)-1):
    star_name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][8])
    radius.append(temp_list[i][9])

df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=['Star_Names','Distance','Mass','Radius'])
df2.to_csv('dwarf_stars.csv')