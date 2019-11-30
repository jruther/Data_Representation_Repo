import requests
import json
from xlwt import*
import csv
 
url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=2019-10-31"


response = requests.get(url)
print(response.status_code)
#print(response.text)

data = response.json()

filename  = 'Bal_mark_reports.json'

data_list = []

with open(filename, 'r') as json_file:
    list_data = json.loads(json_file.read())
    for x in list_data:
        print("ResourceName")





# filename  = 'Bal_mark_reports.json'

# if filename:
#     with open(filename,'w') as f:
#         json.dump(data, f, indent=4)