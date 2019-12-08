import requests
import csv
from bs4 import BeautifulSoup
from xlwt import*


url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from=2019-12-05T23:00;to=2019-12-06T22:00"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')


w = Workbook()
ws = w.add_sheet('Hourly_Windspeeds')

row = 0
ws.write(row, 0, "Datetime")
ws.write(row, 1, "Windspeed")
row += 1


listings = soup.findAll("time")
#print(listings)

for listing in listings:
    fromtime = listing["from"]
    if fromtime:
        #ws.write(row,1, fromtime)
        
        windspeedelem = listing.find("windSpeed")
        if windspeedelem:
            mps = windspeedelem["mps"]
            fromtime = listing["from"]
            ws.write(row,0, fromtime)
            ws.write(row,1, mps)
            row +=1
w.save('finalattempt.xls')

