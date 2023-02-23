import user_input as ui
import db_Interface as dbi
import KNN_functions as KNN
import numpy as np
import os
import main_export_to_excel as mete

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
    if k > len(HSVArr):
        raise Exception("k is less than the length of the training database. You need more training data. Please fix the training database")

    ClassifyData = KNN.file_AverageHSV(filepath)
    #print(ClassifyData)
    z_hat = KNN.knnclassify_bme(labels, HSVArr, ClassifyData, k)
    return z_hat

if __name__ == "__main__":

    day, barcode = ui.get()
    filepath = rf"C:\\DatesWorkspace\\DateIQP\\MyApp\\DateImages\\{day}_{barcode}\\"
    k = 25
    #do not make k < 2
    z_hat = Classify(filepath, k)
    i = 0
    for date in os.listdir(filepath):
        dbi.dbDateEdit(rf"{filepath}date_{i+1}.jpg", int(z_hat[i]))
        print(int(z_hat[i]))
        i += 1
    print( rf"{filepath}date_{i+1}.jpg")
    mete.main(day,barcode)
    print("excell sheet finished with classifications:")
    print(z_hat)