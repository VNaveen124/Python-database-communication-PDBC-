#selectex1.py
#program for reading the records from table
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root",
														database="batch4pm")
	cur=con.cursor()
	sq="select * from student"
	cur.execute(sq)
	print("-------------------------------------------------")
	print("Student Records")
	print("-------------------------------------------------")
	kvr=cur.fetchall()
	for rec in kvr:
		for val in rec:
			print("{}".format(val), end=" ")
		print("\n")
	print("-------------------------------------------------")
except mysql.connector.DatabaseError as db:
	print("Problem in Data base: ",db)
