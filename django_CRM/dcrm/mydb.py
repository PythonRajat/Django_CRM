import mysql.connector
#https://www.youtube.com/watch?v=t10QcFx7d5k&t=92s
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