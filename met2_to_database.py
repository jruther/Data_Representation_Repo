import requests
#import csv
from bs4 import BeautifulSoup
#from xlwt import*
#import pandas as pd 
#from pandas import DataFrame as df
#import numpy as np 
#import mysql.connector


# default_authentication_plugin="mysql_native_password"

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="datarepresentation"
# )
from datetime import datetime
from datetime import timedelta

# today = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

# tomorrow = today + timedelta(days=1)

# print(today)
# print(tomorrow)



import datetime
import time
import numpy as np



# print ('Dates:')
# d1 = datetime.datetime.today()
# print (d1)
# d2 = datetime.datetime.today() + datetime.timedelta(days=1)
# print (d2)

# now = datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
# print(now)

# url = "http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617" + ";from='d1';to='d2'"


# page = requests.get(url)
# print(page.status_code)

# # soup = BeautifulSoup(page.content, 'xml')

# # print(soup)


# print ('Dates:')
# d1 = datetime.datetime.today()
# print (d1)
# d2 = datetime.datetime.today() + datetime.timedelta(days=1)
# print (d2)

# now = datetime.datetime.today().strftime('%Y-%m-%d-%H:%M')
# print(now)

# #tomorrow = now + datetime.timedelta(hours=24)
# print(tomorrow)


# Get the first date and set the time to 11pm.
#start_date = dates.astype('datetime64[ns]')[0] + np.timedelta64(23, 'h')
# Get the end time by adding 24hrs to start_date.
#end_date = start_date + np.timedelta64(24, 'h')



start_date = datetime.datetime.today()#.strftime('%Y-%m-%d-%H:%M')

end_date = start_date + timedelta(minutes = 1440)

#print(start_date)
#print(end_date)

T1 = start_date.strftime('%Y-%m-%dT%H:%M')
T2 = end_date.strftime('%Y-%m-%dT%H:%M')
print(T1)
print(T2)


url="http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from="+T1+";to="+T2"

page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.content, 'xml')

print(soup)