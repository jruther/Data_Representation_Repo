import requests
from xlwt import*
import csv
import xml.etree.ElementTree as ET


url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from=2019-11-27T23:00;to=2019-11-28T22:00"


response = requests.get(url)
print(response.status_code)

root = ET.fromstring(response.text)

tree = ET.ElementTree(root)

tree.write("MetWeather.xml")

tree = ET.parse("MetWeather.xml")


w = Workbook()
ws = w.add_sheet('Hourly_Windspeeds')

row = 0
ws.write(row, 0, "Datetime")
ws.write(row, 1, "Windspeed")
row += 1
for result in tree["pointData"]:
     ws.write(row,0, result["from"])
     ws.write(row,1, result["mps"])
     row += 1

w.save('MetData.xls')















