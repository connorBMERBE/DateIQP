import numpy as np
import cv2
import glob


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
            if not val:
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
def file_AverageHSV(filepath, labelsArr):
    labeled_avgs = []
    count = 0
    imgs = glob.glob(filepath, *.jpg, recursive = False)
    for img in filepath:
        labeled_avgs = np.append(labeled_avgs, np.append(averageHSV(img), count), axis = 0)
        count += 1
    return labeled_avgs


