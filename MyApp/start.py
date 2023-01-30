class IsolateDate: 
    def __init__(self, image, display_huh):
        self.image = image
        self.display_huh = display_huh
        
        self.t1 = 85
        self.t2 = 255

        self.all_interim_images = [image]
        
    def contour_method(self): 
        img = self.image 

        # - here is blur and then convert to greyscale
        imgBlur = cv2.GaussianBlur(img, (7,7), 1)
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_RGB2GRAY)
        
        # - canny edge detector 
        # threshold1 = cv2.getTrackbarPos("threshold1","Parameters")
        # threshold2 = cv2.getTrackbarPos("threshold2","Parameters") 
        imgCanny = cv2.Canny(imgGray, self.t1, self.t2)
        
        # - removing nouse from Canny edges (6:00 min) # use a dialation function, use a kernal 
        kernel = np.ones((5,5)) 
        imgDil = cv2.dilate(imgCanny, kernel, iterations=1) # dialation 
        
        # - getting the actual contour 
        imgContour = img.copy() # where to write with contours
        
        # ---------------------------------
        # - getContours(imgDil, imgContour)
        img = imgDil
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
                
                # -  bounding box (15:30)
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(imgContour, (x, y), (x+w,y+h), (0,255, 0), 5)
                
                cv2.putText(imgContour,  "Perimeter: " + str(peri), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX,0.7, (0,255,0), 2)
                cv2.putText(imgContour,       "Area: " + str(area), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX,0.7, (0,255,0), 2)
                cv2.putText(imgContour, "Approx Len: " + str(len(approx)), (x+w+20, y+70), cv2.FONT_HERSHEY_COMPLEX,0.7, (0,255,0), 2)
        
        return imgContour
        # return just_the_date_image
    
    def image_subtraction_method(): 
        pass


    # def display_contour_method():
    #     cv2.namedWindow("Parameters",cv2.WINDOW_NORMAL)
    #     cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
    #     cv2.resizeWindow("Parameters",640,240)
        
    #     cv2.createTrackbar("threshold1","Parameters",85,300,lambda _:_)
    #     cv2.createTrackbar("threshold2","Parameters",255,300,lambda _:_) # initial value, max value        
    #     cv2.createTrackbar("MaxArea","Parameters",int(totalImgArea/16),totalImgArea, lambda _:_)
    #     cv2.createTrackbar("MinArea","Parameters",5000,totalImgArea, lambda _:_)


# --- 

import cv2 
import numpy as np

img = cv2.imread(".\\..\\ImageAssets\\normal_date.JPG")
img = cv2.resize(img, (800,800)) 


ID = IsolateDate(img, display_huh=True)

just_the_date_image = ID.contour_method()


cv2.imshow("Results", just_the_date_image)

key = cv2.waitKey(0)
# if key == ord('q') or key == 27:
#     break


