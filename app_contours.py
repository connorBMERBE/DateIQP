# https://www.youtube.com/watch?v=Fchzk1lDt7Q

import cv2
import numpy as np

frameWidth = 800
frameHeight = 800

totalImgArea = frameWidth * frameHeight

image = cv2.imread("C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg")
image = cv2.resize(image, (frameWidth,frameHeight))
# image = image[300:500, 300:500] # crop to just the date

cv2.namedWindow("Parameters")
cv2.namedWindow("Result1", cv2.WINDOW_NORMAL)
cv2.namedWindow("Result2", cv2.WINDOW_NORMAL)
cv2.namedWindow("Result3", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("threshold1","Parameters",120,255,lambda _:_)
cv2.createTrackbar("threshold2","Parameters",130,255,lambda _:_) # initial value, max value
cv2.createTrackbar("MaxArea","Parameters",int(totalImgArea/16),totalImgArea, lambda _:_)
cv2.createTrackbar("MinArea","Parameters",5000,totalImgArea, lambda _:_)


def getContours(img, imgContour): #first is input img to detect contours, second we are going to write them into 
    
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    # - removing excess contours (12:00) 
    for cnt in contours: 
        area = cv2.contourArea(cnt)
        
        areaMax = cv2.getTrackbarPos("MaxArea","Parameters")
        areaMin = cv2.getTrackbarPos("MinArea","Parameters")
        
        if areaMax > area > areaMin: # 100 pixels? 
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 7)
            
            # draw perimeter 
            peri = cv2.arcLength(cnt, True) # True being that the contour is closed
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True) # True still closed contours  # using approx, we determine the shape of the object. (Square, triangle, etc) 
            print(len(approx)) 
            
            # -  bounding box (15:30)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x+w,y+h), (0,255, 0), 5)

            cv2.putText(imgContour, "Points: " + str(len(approx)), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX,0.7, (0,255,0), 2)
            cv2.putText(imgContour,   "Area: " + str(len(approx)), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX,0.7, (0,255,0), 2)
            




def main ():
    img = image 
    
    # - here is blur and then convert to greyscale
    imgBlur = cv2.GaussianBlur(img, (7,7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_RGB2GRAY)
    
    # - canny edge detector 
    threshold1 = cv2.getTrackbarPos("threshold1","Parameters")
    threshold2 = cv2.getTrackbarPos("threshold2","Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    
    # - removing nouse from Canny edges (6:00 min) # use a dialation function, use a kernal 
    kernel = np.ones((5,5)) 
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1) # dialation 
    
    # - getting the actual contour 
    imgContour = img.copy() # where to write with contours
    getContours(imgDil, imgContour)
        
    
    return cv2.hconcat([img,imgBlur]), imgDil, imgContour


# -- setup complete 

while True: 
    
    try:
        i1, i2, i3 = main()
    except: 
        import sys
        sys.exit()
    
    # - show and wrap up 
    cv2.imshow("Result1", i1) 
    cv2.imshow("Result2", i2)
    cv2.imshow("Result3", i3)
    key = cv2.waitKey(30)
    if key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()


