import cv2

#i = "israel_national_water.png"
i = "blistered_date.jpg"

img = cv2.imread('assets/'+i, -1)

# img = cv2.resize(img, (800,800))
# img = cv2.resize(img, (0,0), fx=2, fy=2) 
# img = cv.rotate

cv2.imshow("ImageName", img)

# close this window
cv2.waitKey(0) # halt execution until key pressed. (delay for 0 seconds) 
cv2.destroyAllWindows() # finish up 

