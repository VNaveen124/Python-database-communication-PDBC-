#createtab.py
import cx_Oracle
try:
	con=cx_Oracle.connect("scott/tiger@localhost/orcl")
	print("Connection Obtained from Oracle DB")
	print("---------------------------------------------------------")
	cur=con.cursor()
	kvrqry="create table student( sno number(3), sname  varchar2(10), marks number(5,2) )"
	cur.execute(kvrqry)	
	print("Student Table created in Oracle Db--verify")
except cx_Oracle.DatabaseError as de:
	print(de)
finally:
	if con!=None:
		print("DB connection Closed:")
		con.close()
