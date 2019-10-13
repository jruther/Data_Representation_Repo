# code for scaping data from SEMO.com  JR. 11.10.19

import requests
import urllib.request
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.sem-o.com/market-data/dynamic-reports/#BM-095")

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

print(soup.title.string)