#dbcontest.py
import cx_Oracle
try:
	kvrcon=cx_Oracle.connect("scott/tiger@localhost/kvrorcl")
except cx_Oracle.DatabaseError as da:
	print("Problem in Getting Connection from Oracle DB")
else:
	print("Python Program obtains connection from Oracle Data base--Successfully:")
finally:
	if kvrcon!=None:
		print("Db connection Closed:");
		kvrcon.close()
	
