import cv2
import numpy
import random

# img = cv2.imread("C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg")
img = cv2.imread("C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg")

img = cv2.resize(img, (800,800))
print(img.shape)

# (4032, 3024, 3)
# height width channels 
# channels are the color space, how many values are representing each pixel color  (BGR)

# # structure 
# [
# [[0,0,0],[255,255,255]], # black pixel, then white pixel in this row of img
# [[0,0,0],[255,255,255]], # black pixel, then white pixel in this row of img
# ]


for i in range(200):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)] 


# moving a section 
tag = img[300:500, 300:500] # copys a section # rows, columns
img[0:200, 0:200] = tag 
img[200:400, 0:200] = tag 
img[400:600, 0:200] = tag 
img[600:800, 0:200] = tag 



cv2.imshow("ImageName", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


