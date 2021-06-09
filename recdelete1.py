#recdelete1.py
#program for deleting record from table with static data
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	print("Connection Obtained from Oracle DB")
	print("---------------------------------------------------------")
	cur=con.cursor()
	kvrqry="delete from student where sno=30"
	cur.execute(kvrqry)	
	con.commit()
	print("Student Record deleted from Student Table--verify")
except cx_Oracle.DatabaseError as de:
	print(de)
finally:
	if con!=None:
		print("DB connection Closed:")
		con.close()
