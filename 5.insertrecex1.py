#insertrecex1.py
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root",
														database="batch4pm")
	print("Coonection Obtained........")
	cur=con.cursor()
	qry="insert into student values(30,'kvr') "
	cur.execute(qry)
	con.commit()
	print("record inserted --verify")
except mysql.connector.DatabaseError as ab:
	print("Problem with Python Program to connect with MySQL:",ab)
