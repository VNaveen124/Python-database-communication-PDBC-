#altertab1.py
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	print("Connection Obtained from Oracle DB")
	print("---------------------------------------------------------")
	cur=con.cursor()
	kvrqry="alter table student add(cname varchar2(10))"
	cur.execute(kvrqry)	
	print("Student Table altered in Oracle Db--verify")
except cx_Oracle.DatabaseError as de:
	print(de)
finally:
	if con!=None:
		print("DB connection Closed:")
		con.close()
