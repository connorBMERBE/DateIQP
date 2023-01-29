import numpy as np
import cv2

img=cv2.imread("DateIQP\\tutorials\\assets\\blank.jpg") #blank image of tray (control variable)
img1=cv2.imread("DateIQP\\tutorials\\assets\\date.jpg") #test image of date on tray
sub=cv2.subtract(img,img1) #subtraction of empty tray from date on tray to isolate date
gray=cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray,(3,3),0)
contours, _= cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
c=max(contours,key=cv2.contourArea)
im = cv2.resize(sub, (800,800)) #resizes image to a readable scale
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(im)
im2 = cv2.resize(img1, (800, 800)) #resizes image to a readable scale
im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
black = np.array([15]) #lower bound
gray = np.array([255]) #upper bound (there is no upper bound)
mask = cv2.inRange(im, black, gray) # true or false (white or black) if a pixel is within range

result = cv2.bitwise_and(im2, im2, mask=mask) # only shows pixels within the mask range in test image for result

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(result, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints) #shows image
cv2.waitKey(0)
