import requests
import csv
from bs4 import BeautifulSoup
from xlwt import*

url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from=2019-12-02T23:00;to=2019-12-03T22:00"


page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')

w = Workbook()
ws = w.add_sheet('Hourly_Windspeeds')

row = 0
ws.write(row, 0, "Datetime")
ws.write(row, 1, "Windspeed")
row += 1

listings = soup.findAll("time")

for listing in listings:
    #print (listing)
    "2019-12-02T23:00:00Z" = listing["from"]
    if "2019-12-02T23:00:00Z":
        ws.write(row,1, fromtime)


    # timeelem = listing.find("from")
    # if timeelem:
    #     hour = timeelem["from"]
    #     ws.write(row,0,hour)
    #     row +=1
    
    windspeedelem = listing.find("windSpeed")
    if windspeedelem:
        mps = windspeedelem["mps"]
        #print (mps)
        ws.write(row,1, mps)
        row += 1

w.save('MetDataAndrew3.xls')

