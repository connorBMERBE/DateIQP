import mysql.connector as sql
import numpy as np
import db_Interface as dbi

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
# cursor.execute(r'insert into trainingdata values("file\\path00", 23.12345678, 2.00000001, 70, 0);')
# cursor.execute(r'insert into trainingdata values("file\\path01", 1, 2, 3, 0);') 
# cursor.execute(r'insert into trainingdata values("file\\path02", 1, 2, 3, 1);') 
# cursor.execute(r'insert into trainingdata values("file\\path03", 1, 2, 3, 1);') 
# cursor.execute(r'insert into trainingdata values("file\\path04", 1, 2, 3, 2);') 
# cursor.execute(r'insert into trainingdata values("file\\path05", 1, 2, 3, 3);') 
# cursor.execute(r'insert into trainingdata values("file\\path06", 170.425425, 78.42356436, 54.4254252, 4);') 
# cursor.execute(r'insert into trainingdata values("file\\path07", 180, 255, 255, 4);') 
# cursor.execute(r'insert into trainingdata values("file\\path08", 0, 0, 0, 3);') 
# cursor.execute(r'insert into trainingdata values("file\\path09", 1, 1, 1, 2);') 
# cursor.execute(r'insert into trainingdata values("file\\path10", 1, 1, 3.45252, 0);') 
# cursor.execute(r'insert into trainingdata values("file\\path11", 10.45754, 20.24436, 30, 1);') 
# cursor.execute(r'insert into trainingdata values("file\\path12", 100, 200, 45.557864, 0);') 
# Show database
# print(cursor)
# mydb.commit()
# array = np.array([])
array = dbi.getTrainingData()
print(array)