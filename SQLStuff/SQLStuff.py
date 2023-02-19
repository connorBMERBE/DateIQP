import mysql.connector as sql
import numpy as np

# Connect to server
mydb = sql.connect(
    host = "localhost",
    user = "Master",
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
cursor.execute("insert into Dates values('proxy\\address','2023-02-18','2023-02-19',000000,12.6,1,0,0,0,0,1,0,0);") 

# Show database
cursor.execute("select * from Dates")
 
# for x in cursor:
#   print(x)