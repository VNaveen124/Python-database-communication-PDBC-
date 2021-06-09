#tabcreate.py
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root",
														database="batch4pm")
	print("Coonection Obtained........")
	cur=con.cursor()
	qry="create table student (stno  int primary key, name varchar(20) not null) "
	cur.execute(qry)
	print("table created --verify")
except mysql.connector.DatabaseError as ab:
	print("Problem with Python Program to connect with MySQL:",ab)
