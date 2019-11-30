import requests
import json
from xlwt import*
import csv
 
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=2019-10-31"


response = requests.get(url)
print(response.status_code)
#print(response.text)

data = response.json()
#print(data)


filename  = 'prices.json'

if filename:
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

for report in data["items"]:
    print["ResourceName"]
     










# users_list = []

#filename  = 'Bal_mark_reports.json'
     
# with open('data','r') as json_file: 
#     user_data = json.loads(json_file.read())
#     for u in user_data:
#         users_list.append(User(**u))    
# print(users_list)
#         








# w = Workbook()
# ws = w.add_sheet('Daily_BM_Price_Files')

# row = 0
# ws.write(row, 0, "DPuG_ID")
# ws.write(row, 1, "ResourceName")
# row += 1
# for report in data["items"]:
#      ws.write(row,0, report["DPuG_ID"])
#      ws.write(row,1, report["ResourceName"])
#      row += 1
# w.save('Daily_BM_reports.xls')