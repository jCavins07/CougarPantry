import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "username",
	pswd = "password"
) 

print(mydb)
