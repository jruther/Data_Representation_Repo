import requests
import csv
from bs4 import BeautifulSoup

url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from=2019-12-01T23:00;to=2019-12-02T22:00"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')



listings = soup.findAll("time")

print(listings)

# for listing in listings:
#     #print (listing)


#     fromtime = listing['from']
#     print (fromtime)
    
#     windspeedelem = listing.find("windSpeed")
#     if windspeedelem:
#         mps = windspeedelem['mps']
#         print (mps)
#     #gotta go

# #print (soup.prettify())