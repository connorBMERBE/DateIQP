# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 11:02:16 2023

@author: matth
"""


# --------- TODO 
# --- create mask 
# subtract image  
# conduct HARSH segmentation on the image to get just the date colors 

# --- goal here is to get outline mask 
# erode outliers, maybe use morph? 
# morph close to get full shape 

# here could also use another library to get outline of points s

# ENSURE only 1 object at this point with contours on binary. Contours do not have to find the interior
# -- if there are more than 1 contour, return to the beginning or throw in an "unsure" bin 

# use binary image as a mask on original image 


def main(img): 
    