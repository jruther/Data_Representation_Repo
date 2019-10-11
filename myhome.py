# code for scaping data from myhome.ie.  JR. 10.10.19

import requests
import csv
from bs4 import BeautifulSoup
url = requests.get("https://www.myhome.ie/residential/mayo/house-for-sale?page=1")
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('myhome.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter = '\t', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
    entryList = []
    price = listing.find(class_= "PropertyListingCard_Price").text 
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard_Address").text 
    entryList.append(address)

    home_writer.writerow(entryList)
home_file.close()

