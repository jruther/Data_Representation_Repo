import requests
import csv
from bs4 import BeautifulSoup
#from xlwt import* 
import mysql.connector
from datetime import datetime
from datetime import timedelta
import datetime
import time


default_authentication_plugin="mysql_native_password"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="datarepresentation"
)


start_date = datetime.datetime.today()

end_date = start_date + timedelta(minutes = 1440)

T1 = start_date.strftime('%Y-%m-%dT%H:%M')
T2 = end_date.strftime('%Y-%m-%dT%H:%M')
# print(T1)
# print(T2)

#url="http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from="+T1+";to="+T2"

url="http://metwdb-openaccess.ichec.ie/metno-wdb2ts/locationforecast?lat=52.588;long=-7.617;from="+T1+";to="+T2


page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.content, 'xml')

#print(soup)

listings = soup.findAll("time")
#print(listings)

for listing in listings:
    fromtime = listing["from"]
    if fromtime:
        #ws.write(row,1, fromtime)
        
        windspeedelem = listing.find("windSpeed")
        if windspeedelem:
            windspeed = windspeedelem["mps"]
            datetime = listing["from"]
            metList = (datetime, windspeed)
            print(metList)

            cursor = db.cursor()
            sql = "insert into weather_forecast (datetime, windspeed) values (%s,%s)"
            values = (metList)

            cursor.execute(sql, values)

            db.commit()
            print ("1 record inserted, ID:", cursor.lastrowid)

