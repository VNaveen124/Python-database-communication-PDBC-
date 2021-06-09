#recinsert1.py
#program for inserting record in table with static data
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	print("Connection Obtained from Oracle DB")
	print("---------------------------------------------------------")
	cur=con.cursor()
	kvrqry="insert into student values(30,'MVR',39.25,'HCU')"
	cur.execute(kvrqry)	
	con.commit()
	print("Student Record Inserted In Student Table--verify")
except cx_Oracle.DatabaseError as de:
	print(de)
finally:
	if con!=None:
		print("DB connection Closed:")
		con.close()
