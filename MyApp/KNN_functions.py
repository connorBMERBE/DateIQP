import numpy as np
import cv2
import os
import math
from scipy import stats as st

def knnclassify_bme(labels, reference, NewData, k):
    # % Inputs:
    # %   labels = y - A n-by-1 vector of class labels, corresponding to data points in X
    #       0 = Dry
    #       1 = Juicy
    #       2 = Moist
    #       3 = Smooth
    # %   reference = X - A n-by-p data matrix
    # %   NewData = T - A m-by-p matrix of reference points, without/needing class labels
    # %   k = k - A scalar (1-by-1) value indicating the number of nearest neighbors
    # %        to be considered.
    # % Outputs:
    # %    z_hat - A m-by-1 vector of estimated class labels for data points in T
    # %
    # % Created by: Adam C. Lammert (2020)
    # % Author: Connor Gaudette (crgaudette@wpi.edu)
    # %
    # % Description: Determine estimated class labels for a matrix of 
    # %               reference points reference, given data points NewData and labels labels 
    # %               using k nearest nieghbors
    z_hat = np.array([])
    #% vector for storing class label predictions


    distance = np.array([])
    #% vector of distances
    distI = distance
    #% vector of indecies that would sort distance
 

    countdata = 0
    #counter variable for the number of loops in the new data loop
    for data in NewData:
        #iterate over all data points in the new data set
            

        countref = 0
        #counter variable for the number of loops in the reference loop
        for point in reference:
            point = [float(point[0]), float(point[1]), float(point[2])]
            # % Iterate over all data points in X. For each data point, calculate the 
            # % distance between it and the current reference point in T. Store the 
            # % distances in the vector 'distance'.
            if countref == 0:
                distance = np.array([math.sqrt((point[0]-data[0])**2 + (point[1]-data[1])**2  + (point[2]-data[2])**2)])
            else:
                distance= np.append(distance, math.sqrt((point[0]-data[0])**2 + (point[1]-data[1])**2  + (point[2]-data[2])**2))
            countref += 1
        
        # % Get neighbor labels - i.e., sort distances, and find class labels of 
        # % k nearest neighbors.
        distI = np.argsort(distance)
        l = np.array([])
        #array of labels for k nearest neighbors

        lCountCount = 0
        #counter variable for the lCount loop
        for lCount in range(k):
            if lCountCount == 0:
                l = int(labels[distI[lCount]])
            else:
                l = np.append(l, int(labels[distI[lCount]]))
            
        # % Determine the class label - i.e., find the most common class label
        # % from among the nearest neighbors
        z_hat = np.append(z_hat, st.mode(l, keepdims = True).mode[0])
        countdata = countdata + 1

    #return only the most common lable (chooses first to appear if two are equally common)
    return z_hat

# testing the function (suggest using over 25 images of each class, the more images the more 
# accurate the algorithm should be)
# replace reference with array from running file_AverageHSV over a file of new isolated images
# reference = np.array([[132.47227227, 107.26908438, 137.31339851],
#              [130.57921283,  78.64344813, 133.71567369], 
#              [125.48677605,  78.84193034, 130.82432647], 
#              [130.11187778, 123.9429369,  138.94235954], 
#              [128.91943248,  93.19049681, 125.24913338], 
#              [139.42157109,  87.98042584, 132.04917219], 
#              [ 97.36471472, 103.98464378, 126.60416277], 
#              [132.28707128,  97.11577491, 124.74455594], 
#              [147.52107665,  71.44290315, 122.03790658], 
#              [142.49707487,  78.75429739, 122.40956941], 
#              [143.78206458,  65.00432157, 124.31684285], 
#              [145.60844707,  77.78495244, 118.47577344], 
#              [150.86488974,  75.29193484, 117.90376108], 
#              [144.12265162,  69.2118389,  133.28409331], 
#              [139.57424496,  59.73688488, 110.62495373], 
#              [142.56040736,  71.44163322, 111.96338505], 
#              [154.47902371, 114.3048257,   36.40330981],
#              [130.99994456, 101.28924421, 117.80132018], 
#              [135.74033824,  83.66406931, 129.0574293 ],
#              [132.15366212,  65.05886402, 118.6504317 ],
#              [119.3729775, 67.86422724, 142.80515648],
#              [121.70259029, 48.93424457, 143.49583489],
#              [122.11598156,  55.28554006, 114.77709677],
#              [119.23401855,  44.93417831, 143.65010426],
#              [ 74.45286438,  80.77151647, 146.45020657],
#              [139.82857389, 114.50677917, 135.44083512],
#              [104.56374863, 107.03447618, 109.26153331],
#              [135.39908889,  72.3290239,  107.99494786],
#              [119.43484761,  47.01321681, 147.92498556],
#              [123.04346315,  94.03055991, 108.91937551],
#              [118.71362361,  47.8846834,  165.7226173 ],
#              [131.43977685,  78.00271279, 114.87646754]])

# the labels that go with the current training data replace these when training new data
# TestClasses = np.array([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])

# testing point should return [1. 2. 3. ]
# NewData = np.array([[137.25588058,  74.52347406, 111.10100348],
#            [128.24730025,  83.77798541,  94.6254064 ],
#            [104.80966448,  52.57674816, 148.68472416]])

# print(knnclassify_bme(TestClasses, reference, NewData, 7))

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
    #print(labeled_avgs)
    return labeled_avgs

# TestClasses = np.array([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])

# reference = file_AverageHSV(".\\ImageAssets\\MATURITY\\AllIsolated\\")
# NewData = file_AverageHSV(".\\ImageAssets\\YaaraTest\\")
# k = 4
#knnclassify_bme(TestClasses, reference, NewData, k)

if __name__ == "__main__":
    try: 
        TestClasses = np.array([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3])
        reference = file_AverageHSV(".\\ImageAssets\\MATURITY\\AllIsolated\\")
        #training images are stored at the file location above
        NewData = file_AverageHSV(".\\ImageAssets\\YaaraTest\\")
        #testing images are stored at the file location above
        k = 7
        #reccomend that the k value be kept just (75-90%) below the number of training images PER A CLASS
        knnclassify_bme(TestClasses, reference, NewData, k)
        print("ran function")
    except Exception as e:
        print(e)
