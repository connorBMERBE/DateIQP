import numpy as np
import cv2

img=cv2.imread("DateIQP\\tutorials\\assets\\blank.jpg") #blank image of tray (control variable)
img1=cv2.imread("DateIQP\\tutorials\\assets\\date.jpg") #test image of date on tray
sub=cv2.subtract(img,img1) #subtraction of empty tray from date on tray to isolate date
im = cv2.resize(sub, (800,800)) #resizes image to a readable scale
im2 = cv2.resize(img1, (800, 800)) #resizes image to a readable scale
im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
black = np.array([15]) #lower bound
gray = np.array([255]) #upper bound (there is no upper bound)
mask = cv2.inRange(im, black, gray) # true or false (white or black) if a pixel is within range
result = cv2.bitwise_and(im2, im2, mask=mask) # only shows pixels within the mask range in test image for result
# Show keypoints
cv2.imshow("Subtraction", result) #shows image
cv2.waitKey(0)
