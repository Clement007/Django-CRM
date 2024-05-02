import mysql.connector

# Create a variable called dataBase
dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Akanyamasyo',

	)
#Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All done!")
