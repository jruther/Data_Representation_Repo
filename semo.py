# code for scaping data from SEMO.com  JR. 11.10.19

import requests
import urllib.request
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.sem-o.com/market-data/dynamic-reports/#BM-095")

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('semo.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="table-responsive semo_table table_fixed-head")


rows = soup.findAll("tr")
for row in rows:
    datalist = []
    cols = row.findAll("td")
    for col in cols:
        datalist.append(col.text)
    print(datalist)

