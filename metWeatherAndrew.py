import requests
import csv
from bs4 import BeautifulSoup
from xlwt import*

url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from=2019-12-01T23:00;to=2019-12-02T22:00"


page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')

w = Workbook()
ws = w.add_sheet('Hourly_Windspeeds')

row = 0
ws.write(row, 0, "Datetime")
ws.write(row, 1, "Windspeed")
ws.write(row,2,"Wind_Strength")
row += 1

listings = soup.findAll("time")

for listing in listings:
    # #print (listing)
    # fromtime = listing["from"]
    # if fromtime:
    #     ws.write(row,0, fromtime)
    #     row +=1
    time = listing.find("from")
    windspeedelem = listing.find("windSpeed")
    if windspeedelem:
        mps = windspeedelem["mps"]
        #time = time["from"] 
        #print (mps)
        ws.write(row,1, mps)
        ws.write(row,2, time)
        row += 1

w.save('MetDataAndrew6.xls')


