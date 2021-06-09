#dbcreate.py
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root")
	print("Coonection Obtained........")
	cur=con.cursor()
	cur.execute("create database batch4pm")
	print("DataBase created --verify")
except mysql.connector.DatabaseError as ab:
	print("Problem with Python Program to connect with MySQL:",ab)
