import requests
import json
from xlwt import*
import csv


url = "http://reports.sem-o.com/api/v1/documents/static-reports"

#url = "http://reports.sem-o.com/api/v1/documents/static-reports/#BM-095"

#url = 'https://www.sem-o.com/market-data/dynamic-reports/#BM-095'

#url = 'http://reports.sem-o.com/api/v1/documents/{REPT_041}'

#url = 'https://reports.sem-o.com/api/v1/documents/static-reports?DPuG_ID=EA-002&ReportName=ETS%20Bid%20File&ResourceName=BidFile_SEM-IDA1_PWR-SEM-GB&Group=Market%20Data&Date=%3E=2019-02-01%3C=2019-02-28&page=1&page_size=10&sort_by=PublishTime&order_by=ASC'


response = requests.get(url)
print(response.status_code)
#print(response.text)

data = response.json()
print(data)






filename  = 'reports.json'

if filename:
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

w = Workbook()
ws = w.add_sheet('reports')
ws.write("data")
w.save('reports.xls')



