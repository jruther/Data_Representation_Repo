import requests
import json
from xlwt import*
import csv

#url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=2019-10-31&ResourceName=PUB_30MinImbalCost_201910312230.xml"
url = "https://reports.sem-o.com/api/v1/documents/PUB_30MinImbalCost_201910312230.xml"

response = requests.get(url)
print(response.status_code)
#print(response.text)
data = response.json()
print(data)

filename  = 'Imbal_price.json'

if filename:
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('Imb_Price')

row = 0
ws.write(row, 0, "StartTime")
ws.write(row, 1, "EndTime")
ws.write(row, 2, "ImbalanceVolume")
ws.write(row, 3, "ImbalancePrice")
ws.write(row, 4, "ImbalanceCost")
row += 1
for report in data["rows"]:
     ws.write(row,0, report["StartTime"])
     ws.write(row,1, report["EndTime"])
     ws.write(row,2, report["ImbalanceVolume"])
     ws.write(row,3, report["ImbalancePrice"])
     ws.write(row,4, report["ImbalanceCost"])
     row += 1

w.save('Imb_Prices.xls')