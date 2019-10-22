# code for scaping data from SherryFitz.ie.  JR. 11.10.19

import requests
import urllib.request
import csv
from bs4 import BeautifulSoup

url = "https://www.sherryfitz.ie/properties/search?search%5Bpage%5D=2&search%5Bproperty_id%5D=false&search%5Btop_location%5D=gMO"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('sherryfitz.csv', mode = 'w')
home_writer = csv.writer(home_file, delimiter = '\t', quotechar = '"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="property-card-container")

for listing in listings:
    entryList = []
    price = listing.find(class_= "property-card-info-price") 
    entryList.append(price.text)
    address = listing.find(class_="property-card-address")
    entryList.append(address.text)

    home_writer.writerow(entryList)
home_file.close()