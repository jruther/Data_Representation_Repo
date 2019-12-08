import requests
import xml.etree.ElementTree as ET
import pandas as pd
from xlwt import*


url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from=2019-12-04T23:00;to=2019-12-05T22:00"


r = requests.get(url)
#print(r.text)

root = ET.fromstring(r.text)

tree = ET.ElementTree(root)

#tree.write('file2.xml') #this writes the file to an xml for ease of viewing open with excel.
  

w = Workbook()
ws = w.add_sheet('Hourly_Windspeeds')

row = 0
ws.write(row, 0, "Datetime")
ws.write(row, 1, "Windspeed")
ws.write(row,2,"Wind_Strength")
row += 1


root = ET.parse('file.xml').getroot()

for node in root:
    hour = node.find("from")
    ws = node.find("mps")
    st = node.find("beaufort")
    ws.write(row,0, hour)
    ws.write(row,1, ws)
    ws.write(row,2, st)
    row += 1
    
w.save('MetJR.xls')
