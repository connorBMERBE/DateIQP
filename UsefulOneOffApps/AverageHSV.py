import numpy as np
import cv2
import os
import TestingHSV as test


## takes in an HSV image and returns a numpy array [average_Hue, average_Saturation, average_Value] 
## where average_Hue is the average hue of every non-black pixel in the image, 
##average_Saturation is the average saturation of every non-black pixel in the image, 
##average_value is the average value of every non-black pixel in the image
def averageHSV(img):
    avg_hue = np.double(0)
    avg_sat = np.double(0)
    avg_val = np.double(0)
    count = 0
    for row in img:
        for item in row:
            hue = item[0]
            sat = item[1]
            val = item[2]
            if val:
                count += 1
                avg_hue += hue
                avg_sat += sat
                avg_val += val
    avg_hue /= count
    avg_sat /= count
    avg_val /= count
    return np.array([avg_hue, avg_sat, avg_val])

## takes in a file name and returns a 2D numpy array [[average_Hue, average_Saturation, average_Value, label],...]
## labels is the position of the order the images was found in the file given
## where average_Hue is the average hue of every non-black pixel in the image, 
## average_Saturation is the average saturation of every non-black pixel in the image, 
## average_value is the average value of every non-black pixel in the image
def file_AverageHSV(filepath): 
    labeled_avgs = np.array([])
    count = 0
    files = os.listdir(filepath)
    for file in files:
        if file.endswith(('.jpg')):
            theImg = cv2.imread(filepath + file)
            theImg = cv2.cvtColor(theImg, cv2.COLOR_BGR2HSV)
            curr_avg = averageHSV(theImg)
            if count == 0:
                labeled_avgs = curr_avg
            else:
                 labeled_avgs = np.vstack((labeled_avgs,curr_avg))
            count += 1
            print(count)
    print(labeled_avgs)
    return labeled_avgs

TestClasses = np.array([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])

reference = file_AverageHSV("DateIQP\\ImageAssets\\MATURITY\\AllIsolated\\")
NewData = file_AverageHSV("DateIQP\\ImageAssets\\YaaraTest\\")
k = 4
test.knnclassify_bme(TestClasses, reference, NewData, k)