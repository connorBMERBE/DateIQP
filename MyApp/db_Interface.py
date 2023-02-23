import mysql.connector as sql
import numpy as np


# Connect to server
mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "D@t3MACHINE",
    database = "datesdb"
    )

# Creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = mydb.cursor()

#add row to dates table
def dbDateAdd( imageAddress, harvestDay, measureDay, barCode, weight):
    cursor.execute(rf'insert into dates values("{imageAddress}", "{harvestDay}", "{measureDay}", {barCode}, {weight}, null, null, null, null, null, null, null, null);')
    mydb.commit()

#delete rows of images in a specific directory from dates table
def dbDateDelete( imageAddress):
    cursor.execute(rf'delete from dates where imageAddress = "{imageAddress}";')
    mydb.commit()

#add row to trainingData table
def dbTrainingAdd( imageAddress, averageHue, averageSaturation, averageValue, classification ):
    cursor.execute(rf"insert into trainingData values('{imageAddress}', {averageHue}, {averageSaturation}, {averageValue}, {classification});")
    mydb.commit()

#update classification of dates in dates table
def dbDateEdit( imageAddress, classification):
    if classification == 0:
        columnName = 'dry'
    elif classification == 1:
        columnName = 'readyOrJuicy'
    elif classification == 2:
        columnName = 'moist'
    elif classification == 3:
        columnName = 'firm'
    elif classification == 4:
        columnName = 'yellow'
    elif classification == 5:
        columnName = 'halfFirm'
    elif classification == 6:
        columnName = 'skippedAStage'
    cursor.execute(rf"update dates set {columnName} = 1 where imageAddress = '{imageAddress}';")
    mydb.commit()

#returns selectedc table information as a 2d array
def getData(statement):
    tableArray = np.array([])
    cursor.execute(statement)
    counter = 0
    for x in cursor:
        if counter == 0:
            tableArray = np.array([x])
        else:
            tableArray = np.vstack((tableArray, np.array([x])))
        counter = counter + 1
    return tableArray

#returns trainingData as a 2d array
def getTrainingData():
    return getData("select * from trainingData;")

#returns dates table as a list harvested on a specific day from a specific tree
def getFilteredDatesData(harvestDay, barCode):
    return getData(rf'select * from dates where harvestDay = "{harvestDay}" AND barCode = {barCode};')
