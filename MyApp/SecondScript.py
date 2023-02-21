import user_input as ui
import DBWrite as dw
import KNN_functions as KNN
import numpy as np

def MakeArrays():
    BigArr = dw.getTrainingData()
    HSVArr = np.array([])
    labels = np.array([])
    for i in range(len(BigArr)):
        if i == 0:
            HSVArr = np.array([BigArr[i][0],BigArr[i][1],BigArr[i][2]])
            labels = np.array([BigArr[i][3]])
        else:
            HSVArr = np.vstack((HSVArr,np.array([BigArr[i][0],BigArr[i][1],BigArr[i][2]])))
            labels = np.vstack((labels, np.array([BigArr[i][3]])))
    
    return HSVArr, labels

def Classify(filepath, k):
    HSVArr, labels = MakeArrays()
    ClassifyData = KNN.file_AverageHSV(filepath)
    z_hat = KNN.knnclassify_bme(labels, HSVArr, ClassifyData, k)
    return z_hat

if __name__ == "__main__":
    day, barcode = ui.get()
    filepath = f".\\DateImages\\{day}_{barcode}\\"
    k = 25
    Classify(filepath, k)
    




