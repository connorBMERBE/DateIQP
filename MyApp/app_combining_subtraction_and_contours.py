import cv2 
import numpy as np
import os 
import sys

class IsolateDate: 
    def __init__(self):       
        pass
        
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

        # ---------- preprocessing
        self.initialize_parameters()

        self.image = img 

        # - here is blur and then convert to greyscale
        imgBlur = cv2.GaussianBlur(img, (7,7), 1)

        # - canny edge detector  
        imgCanny = cv2.Canny(imgBlur, self.t1, self.t2)
        # return imgCanny
        
        # - removing nouse from Canny edges (6:00 min) # use a dialation function, use a kernal 
        kernel = np.ones((5,5)) 
        imgDil = cv2.dilate(imgCanny, kernel, iterations=1) # dialation 
        
        # ---------- postprocessing
        # - Get Contours 
        contours, hierarchy = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        # - removing excess contours (12:00) 
        filtered_contours = []
        for cnt in contours: 
            if self.areaMax > cv2.contourArea(cnt) > self.areaMin: # 100 pixels? 
                filtered_contours.append(cnt)
        
        # - create mask from contours and isolate pixels     
        mask = np.zeros(imgDil.shape, np.uint8)
        cv2.drawContours(mask, filtered_contours, -1, (255,255,255), -1 )        
        # return mask
        
        just_the_date_image = cv2.bitwise_and(img, img, mask=mask)
        return just_the_date_image 
        
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

    def bounding_mask_pixels(self, img):
        self.image = img 
        
        

def main():
    # - create window environment
    cv2.namedWindow("Parameters",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Parameters",640,240)
    
    cv2.createTrackbar("threshold1","Parameters",85,300,lambda _:_)
    cv2.createTrackbar("threshold2","Parameters",255,300,lambda _:_) # initial value, max value        
    cv2.createTrackbar("MaxArea","Parameters",40_000,1_000_000, lambda _:_)
    cv2.createTrackbar("MinArea","Parameters",5000,1_000_000, lambda _:_)
    
    # - load images 
    blank_address = ".\\..\\ImageAssets\\Empty\\Empty1.jpg"
    
    imdir = '.\\..\\ImageAssets\\'
    files = os.listdir(imdir)
    image_paths = list(
        map(lambda filename: imdir+filename, 
            filter(
                lambda filename: filename.endswith(('.jpg','.JPG')), files)
            )
        )
    
    cv2.createTrackbar("Image","Parameters",0,len(image_paths)-1, lambda _:_)
    
    # ---- do the program 
    ID = IsolateDate() 

    while True: 
        img = cv2.imread(image_paths[cv2.getTrackbarPos("Image","Parameters")])
        img = cv2.resize(img, (800,800)) 
        
        # just_the_date_image = ID.contour_method(img) 
        # just_the_date_image = ID.image_subtraction_method(img, blank_address) 
        # just_the_date_image = ID.both(img, blank_address)
        just_the_date_image = ID.bounding_mask_pixels(img) 
    
        cv2.imshow("Results", just_the_date_image) 
        key = cv2.waitKey(30) 
        if key == ord('q') or key == 27:
            break
    cv2.destroyAllWindows()

main()