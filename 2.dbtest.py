#dbtest.py
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root")
	if (con.is_connected()):
		print("Python Program connected to MySql Database")
except mysql.connector.DatabaseError as ab:
	print("Problem with Python Program to connect with MySQL:",ab)
