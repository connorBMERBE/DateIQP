import mysql.connector as sql
import numpy as np

# Connect to server
mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "D@t3MACHINE",
    database = "datesdb"
)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

# Creating a database with a name
# 'geeksforgeeks' execute() method
# is used to compile a SQL statement
# below statement is used to create
# the 'geeksforgeeks' database
cursor.execute("insert into testing values(9);") 
cursor.execute("insert into testing values(6);")
# Show database
print(cursor)
mydb.commit()
cursor.execute("select * from testing;")
for x in cursor:
  print(x)
cursor.execute("drop table testing;")