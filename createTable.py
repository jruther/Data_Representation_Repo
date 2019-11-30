import mysql.connector

default_authentication_plugin="mysql_native_password"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="datarepresentation"
)
cursor = db.cursor()
sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

cursor.execute(sql)