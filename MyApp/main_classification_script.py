import user_input as ui
import db_Interface as dbi
import KNN_functions as KNN
import numpy as np
import os

def MakeArrays():
    BigArr = dbi.getTrainingData()
    HSVArr = np.array([])
    labels = np.array([])
    for i in range(len(BigArr)):
        if i == 0:
            HSVArr = np.array([BigArr[i][1],BigArr[i][2],BigArr[i][3]])
            labels = np.array([BigArr[i][4]])
        else:
            HSVArr = np.vstack((HSVArr,np.array([BigArr[i][1],BigArr[i][2],BigArr[i][3]])))
            labels = np.vstack((labels,  np.array([BigArr[i][4]])))
    
    return HSVArr, labels

def Classify(filepath, k):
    HSVArr, labels = MakeArrays()
    ClassifyData = KNN.file_AverageHSV(filepath)
    z_hat = KNN.knnclassify_bme(labels, HSVArr, ClassifyData, k)
    return z_hat

if __name__ == "__main__":
    day, barcode = ui.get()
    filepath = rf"C:\DatesWorkspace\DateIQP\MyApp\DateImages\{day}_{barcode}" + "\\"
    k = 5
    z_hat = Classify(filepath, k)
    print(filepath)
    i = 1
    for date in os.listdir(filepath):
        dbi.dbDateEdit(f"{filepath}image_{i}.jgp", z_hat[i])
        i += 1