import mysql.connector

databse = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin@123'
)

#prepare a cursor object
cursorObject = databse.cursor()

#create a database
cursorObject.execute("CREATE DATABASE webdata1;")

print("All done!")