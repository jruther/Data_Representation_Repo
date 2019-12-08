import mysql.connector

default_authentication_plugin="mysql_native_password"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")

