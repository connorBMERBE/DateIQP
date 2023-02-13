import numpy as np
import cv2
import os
import random as rand


## takes in an HSV image and returns a numpy array [average_Hue, average_Saturation, average_Value] 
## where average_Hue is the average hue of every non-black pixel in the image, 
##average_Saturation is the average saturation of every non-black pixel in the image, 
##average_value is the average value of every non-black pixel in the image
def averageHSV(img):
    avg_hue = 0
    avg_sat = 0
    avg_val = 0
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
    return [avg_hue, avg_sat, avg_val]

## takes in a file name and returns a 2D numpy array [[average_Hue, average_Saturation, average_Value, label],...]
## labels is the position of the order the images was found in the file given
## where average_Hue is the average hue of every non-black pixel in the image, 
## average_Saturation is the average saturation of every non-black pixel in the image, 
## average_value is the average value of every non-black pixel in the image
def file_AverageHSV(filepath, classLabels): 
    #readd weight labels
    labeled_avgs = []
    count = 0
    files = os.listdir(filepath)
    for file in files:
        if file.endswith(('.jpg')):
            theImg = cv2.imread(filepath + file)
            theImg = cv2.cvtColor(theImg, cv2.COLOR_BGR2HSV)
            curr_avg = averageHSV(theImg)
            curr_avg.append(count)
            #curr_avg.append(weightLabels[count])
            curr_avg.append(classLabels[count])
            #print(curr_avg)
            labeled_avgs.append(curr_avg)
            count += 1
    print(labeled_avgs)
    #return labeled_avgs

cLRand = []
wLRand = []
i = 0
while i < 8:
    cLRand.append(rand.randint(1,6))
    wLRand.append(rand.randint(1,20))
    i = i+1

file_AverageHSV("C:\\Users\\conno\\OneDrive\\Desktop\\IQP\\IQP\\DateIQP-1\\ImageAssets\\Juicy\\",wLRand,cLRand)
    