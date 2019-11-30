import mysql.connector

default_authentication_plugin="mysql_native_password"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    #auth_plugin='mysql_native_password'
)
cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")

