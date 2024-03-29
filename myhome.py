# code for scaping data from myhome.ie.  JR. 10.10.19

import requests
import urllib.request
import csv
from bs4 import BeautifulSoup
#Url = requests.get("https://www.myhome.ie/residential/mayo/house-for-sale?page=1")
page = requests.get("https://www.myhome.ie/residential/mayo/house-for-sale?page=1")

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('myhome.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter = '\t', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryList = []
    price = listing.find(class_= "PropertyListingCard_Price") 
    entryList.append(price.text)
    address = listing.find(class_="PropertyListingCard_Address")
    entryList.append(address.text)

    home_writer.writerow(entryList)
home_file.close()

