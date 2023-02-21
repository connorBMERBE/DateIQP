import mysql.connector as sql
import numpy as np
import datetime as dt

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

#add row to dates table
def dbDateAdd( imageAddress, harvestDay, measureDay, barCode, weight):
    cursor.execute(f'insert into dates values({imageAddress}, {harvestDay}, {measureDay}, {barCode}, {weight});')
    mydb.commit()

#add row to trainingData table
def dbTrainingAdd( imageAddress, averageHue, averageSaturation, averageValue, classification ):
    cursor.execute(f'insert into trainingData values({imageAddress}, {averageHue}, {averageSaturation}, {averageValue}, {classification});')
    mydb.commit()

#update classification of dates in dates table
def dbDateEdit( imageAddress, classification):
    columnName = ''
    if classification == 0:
        columName = 'dry'
    elif classification == 1:
        columName = 'readyOrJuicy'
    elif classification == 2:
        columName = 'moist'
    elif classification == 3:
        columName = 'firm'
    elif classification == 4:
        columName = 'yellow'
    elif classification == 5:
        columName = 'halfFirm'
    elif classification == 6:
        columName = 'skippedAStage'
    cursor.execute(f'update dates set {columnName} = 1 where imageAddress = {imageAddress};')
    mydb.commit()

def getTrainingData():
    trainingArray = np.array([])
    cursor.execute("select * from trainingData;")
    counter = 0
    for x in cursor:
        if counter == 0:
            trainingArray = np.array([x])
        else:
            trainingArray = np.vstack((trainingArray, np.array([x])))
    counter = counter + 1
    return trainingArray