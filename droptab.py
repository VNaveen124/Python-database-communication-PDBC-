#droptab.py
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	print("Connection Obtained from Oracle DB")
	print("---------------------------------------------------------")
	cur=con.cursor()
	kvrqry="drop table student"
	cur.execute(kvrqry)	
	print("Student Table Dropped in Oracle Db--verify")
except cx_Oracle.DatabaseError as de:
	print(de)
finally:
	if con!=None:
		print("DB connection Closed:")
		con.close()
