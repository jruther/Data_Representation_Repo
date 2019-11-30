import mysql.connector

default_authentication_plugin="mysql_native_password"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="datarepresentation"
)

cursor = db.cursor()
sql = "delete from student where id = %s"
values = (2,)

cursor.execute(sql, values)

db.commit()
print ("OK")