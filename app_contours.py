# https://www.youtube.com/watch?v=Fchzk1lDt7Q

import cv2
# import numpy as np

frameWidth = 800
frameHeight = 800

image = cv2.imread("C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg")
image = cv2.resize(image, (frameWidth,frameHeight))


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("threshold1","Parameters",150,255,lambda _:_)
cv2.createTrackbar("threshold2","Parameters",255,255,lambda _:_)


# -- 

def main():
    img = image 
    
    # here is blur and then convert to greyscale
    imgBlur = cv2.GaussianBlur(img, (7,7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_RGB2GRAY)
    
    # canny edge detector 
    threshold1 = cv2.getTrackbarPos("threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    
    
    cv2.imshow("Result", img)
    cv2.imshow("blur", imgBlur)
    cv2.imshow("grey", imgGray)
    if cv2.waitKey(0) == ord('q'):
        import sys; sys.exit();  
    

main()

