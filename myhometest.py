# code for scaping data from myhome.ie.  JR. 10.10.19

import requests
import csv
from bs4 import BeautifulSoup


#url = requests.get("https://www.myhome.ie") #for some reason my terminal doesn't like 'url'

page = requests.get("https://www.myhome.ie")

soup1 = BeautifulSoup(page.content, 'html.parser')



print(page)
print("---------------------------")
print(soup1.prettify())