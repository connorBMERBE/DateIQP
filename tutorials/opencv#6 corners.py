import numpy as np 
import cv2

img = cv2.imread('C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg')
img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey, 100, 0.6, 10) # img, quality of corner range, minimum euclidian distance in pixels 
print(corners)
corners = np.int0(corners)

for corner in corners: 
    print(corner) 
    x,y = corner.ravel() 
    cv2.circle(img, (x,y), 5, (255, 0, 0), -1) 

cv2.imshow("Frame", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

