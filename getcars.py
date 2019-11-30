import requests
import json
from xlwt import*



url = "http://127.0.0.1:5000/carviewer.html"

response = requests.get(url)
print(response.status_code)
print(response.text)

#data = response.json()

#print(data)

# filename  = 'reports.json'

# if filename:
#     with open(filename,'w') as f:
#         json.dump(data, f, indent=4)

# w = Workbook()
# ws = w.add_sheet('reports')
# ws.write(data)
# w.save('reports.xls')