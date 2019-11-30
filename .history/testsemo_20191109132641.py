import requests
import json
from xlwt import*
import csv

#url = "http://reports.sem-o.com/api/v1/documents/static-reports?Dynamic=true"

#url = 'https://reports.sem-o.com/api/v1/documents/static-reports?=false&DPuG_ID=EA-002&ReportName=ETS%20Bid%20File&ResourceName=BidFile_SEM-IDA1_PWR-SEM-GB&Group=Market%20Data&Date=%3E=2019-02-01%3C=2019-02-28&page=1&page_size=10&sort_by=PublishTime&order_by=ASC'

#url = "http://reports.sem-o.com/api/v1/documents/dynamic-reports" - THIS DOESN'T EXIST!!

#url = "http://reports.sem-o.com/api/v1/documents/static-reports/#BM-095"

#url = 'https://www.sem-o.com/market-data/dynamic-reports'

#url = 'https://reports.sem-o.com/api/v1/documents/static-reports?DPuG_ID=EA-002&ReportName=ETS%20Bid%20File&ResourceName=BidFile_SEM-IDA1_PWR-SEM-GB&Group=Market%20Data&Date=%3E=2019-02-01%3C=2019-02-28&page=1&page_size=10&sort_by=PublishTime&order_by=ASC'

url = "http://reports.sem-o.com/api/v1/documents/static-reports"

#url = "http://reports.sem-o.com/documents"

response = requests.get(url)
print(response.status_code)
print(response.text)

#data = response.json()
#print(data)

# filename  = 'all_reports.json'

# if filename:
#     with open(filename,'w') as f:
#         json.dump(data, f, indent=4)

# w = Workbook()
# ws = w.add_sheet('all_reports')

# row = 0
# ws.write(row, 0, "DPuG_ID")
# ws.write(row, 1, "ReportName")
# row += 1
# for report in data["items"]:
#      ws.write(row,0, report["DPuG_ID"])
#      ws.write(row,1, report["ReportName"])
#      row += 1

# w.save('all_reports.xls')



