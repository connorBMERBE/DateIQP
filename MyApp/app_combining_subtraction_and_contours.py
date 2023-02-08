class IsolateDate: 
    def __init__(self, display_huh=True):
        self.display_huh = display_huh
        
        self.all_interim_images = []
    
        cv2.namedWindow("Parameters",cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Parameters",640,240)
        
        cv2.createTrackbar("threshold1","Parameters",85,300,lambda _:_)
        cv2.createTrackbar("threshold2","Parameters",255,300,lambda _:_) # initial value, max value        
        cv2.createTrackbar("MaxArea","Parameters",40_000,1_000_000, lambda _:_)
        cv2.createTrackbar("MinArea","Parameters",5000,1_000_000, lambda _:_) 
    
    def initialize_parameters(self):
        # -- setup 
        # self.t1 = 85
        # self.t2 = 255
        self.t1 = cv2.getTrackbarPos("threshold1","Parameters")
        self.t2 = cv2.getTrackbarPos("threshold2","Parameters") 

        # self.areaMax = 40_000 
        # self.areaMin = 5_000 
        self.areaMax = cv2.getTrackbarPos("MaxArea","Parameters")
        self.areaMin = cv2.getTrackbarPos("MinArea","Parameters")
             
        
    def contour_method(self, img): 

        self.initialize_parameters()

        self.image = img 

        # - here is blur and then convert to greyscale
        imgBlur = cv2.GaussianBlur(img, (7,7), 1)
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_RGB2GRAY)
        
        # - canny edge detector  
        imgCanny = cv2.Canny(imgGray, self.t1, self.t2)
        
        # - removing nouse from Canny edges (6:00 min) # use a dialation function, use a kernal 
        kernel = np.ones((5,5)) 
        imgDil = cv2.dilate(imgCanny, kernel, iterations=1) # dialation 
        
        # ---------------------------------
        # - getContours(imgDil, imgContour)
        contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        # - getting the actual contour 
        imgContour = img.copy() # where to write with contours
        
        # - filtering countours - removing excess contours (12:00)
        # def filterme(): 
        #     within_area = self.areaMax > area > self.areaMin
        #     return within_area
        
        # filter(filterme, contours)
        
        # - removing excess contours (12:00) 
        for cnt in contours: 
            area = cv2.contourArea(cnt)
            
            if self.areaMax > area > self.areaMin: # 100 pixels? 
                
                # --- isolateme! 
                
                
                # --- drawme! 
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
        
        
        # check this out for image contouring heierachy help, can potentially determine the closed contours 
        # https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html
    
    def image_subtraction_method(self, img, blank_address): 
        self.image = img
        # Load in the images from the file:
        control=cv2.imread(blank_address) #blank image of tray (control variable)
        control = cv2.resize(control, self.image.shape[0:2]) # resize to shape of self.image
           
        sub=cv2.subtract(control,self.image) #Creating the mask # subtraction of empty tray from date on tray to isolate date
        
        sub = cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY) #makes subtraction grayscale to create a mask
        black = np.array([15]) #lower bound
        white = np.array([255]) #upper bound (there is no upper bound)
        mask = cv2.inRange(sub, black, white) # true or false (white or black) if a pixel is within range
        result = cv2.bitwise_and(self.image, self.image, mask=mask) # only shows pixels within the mask range in test image for result

        return result 
    
    def both(self, img, blank_address):
        self.image = img
        return self.contour_method(self.image_subtraction_method(img, blank_address))

# --- 

import cv2 
import numpy as np

# img = cv2.imread(".\\..\\ImageAssets\\normal_date.JPG")
# img = cv2.imread(".\\..\\ImageAssets\\blistered_date.JPG")

# img = cv2.imread(".\\..\\ImageAssets\\date.JPG")
# blank_address = ".\\..\\ImageAssets\\blank.jpg"

img = cv2.imread(".\\..\\ImageAssets\\subtraction\\full.jpg")
blank_address = ".\\..\\ImageAssets\\subtraction\\empty.jpg"

img = cv2.resize(img, (800,800)) 
ID = IsolateDate() 

# ---- call main and cleanup 
while True: 
    # just_the_date_image = ID.contour_method(img) 
    # just_the_date_image = ID.image_subtraction_method(img, blank_address) 
    just_the_date_image = ID.both(img, blank_address)

    cv2.imshow("Results", just_the_date_image) 
    key = cv2.waitKey(30) 
    if key == ord('q') or key == 27:
        break
cv2.destroyAllWindows()

