import pyodbc
conn= r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Administrator\Documents\Database1.accdb;'
conn_1=pyodbc.connect(conn)

cursor= conn_1.cursor()
DATA= cursor.execute("select * from department")
print(DATA.fetchall())