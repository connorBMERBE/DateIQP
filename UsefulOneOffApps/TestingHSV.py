import numpy as np
import cv2
import os
import random as rand
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
    # %               reference points T, given data points X and labels y
    #% Setup
    #m = len(NewData)
    # number of data points in T
    #n = len(reference)
    # number of data points in X
    z_hat = np.array([])
    # zeros(m,1)
    #% vector for storing class label predictions
    distance = np.array([])
    distI = distance
    #% vector of distances

    #% Iterate over all reference points in T
    countdata = 0
    for data in NewData:
            
        # % Iterate over all data points in X. For each data point, calculate the 
        # % distance between it and the current reference point in T. Store the 
        # % distances in the vector 'distance'.
        countref = 0
        for point in reference:
            #%distance(jtor) = ;
            #point = [h,s,v]
            #distance = sqqrt((h1-h2)^2 + (s1-s2)^2 + (v1-v2)^2)
            distance= np.append(distance, math.sqrt((point[0]-data[0])**2 + (point[1]-data[1])**2  + (point[2]-data[2])**2))
            countref += 1
        
        # % Get neighbor labels - i.e., sort distances, and find class labels of 
        # % k nearest neighbors.
        distI = np.argsort(distance)
        l = np.array([]*k)

        for lCount in range(len(l)):
            l[lCount] = distance[distI[lCount]]
            
        # % Determine the class label - i.e., find the most common class label
        # % from among the nearest neighbors
        z_hat = np.append(z_hat, st.mode(l, keepdims=None).mode)
        countdata = countdata + 1
        print(z_hat)
    return z_hat
