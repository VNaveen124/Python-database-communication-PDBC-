#dynamicrecdelete1.py
#program for deleting record from table with dynamic  data
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",
														user="root",
														passwd="root",
														database="batch4pm")
	cur=con.cursor()
	while(True):
		try:
			print("---------------------------------------------------------")
			stno=int(input("Enter Student Number for deleting a record:"))
			qry="delete from student where stno=%d "
			cur.execute(qry %stno)
			con.commit()
			print("---------------------------------------------------------")
			print("Student Record deleted:")
			print("---------------------------------------------------------")
			ch=input("Do u want delete another record(yes/no):")
			if(ch=="no"):
				break
		except ValueError:
			print("Don't enter strs/ special symbols/ alpha-numeric values:")

except mysql.connector.DatabaseError as de:
	print(de)
