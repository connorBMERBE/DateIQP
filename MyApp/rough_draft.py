# --------- TODO 
# --- create mask 
# subtract image  
# conduct segmentation on the image to get just the date colors 

# --- goal here is to get outline mask 
# erode outliers, maybe use morph? 
# morph close to get full shape 
# use contours to isolate the largest contour, which at this point should definitely be the date 

# here could also use another library to get border of all points, without having to morph or contour
# use binary image as a mask on original image 

import cv2 
import numpy as np 
import helper_functions

shape = (3840,2160)
# shape = (800, 800)

subtraction_parameter = 100 # mask on subtraction 
size_of_ellipse = 50
lowHSV = (180-45, 60, 50)
highHSV = (180, 255, 255) # use app_morphology or app_HSV_Thresholds_on_Image

def get_me_a_date(img, blank_img ,stops_huh=False):
    if stops_huh:
        cv2.imshow("Results", img); cv2.waitKey(0)

    # - subtraction         
    sub = cv2.subtract(blank_img,img) 
    if stops_huh:
        cv2.imshow("Results", sub); cv2.waitKey(0)
    
    sub = cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY) #makes subtraction grayscale to create a mask
    if stops_huh:
        cv2.imshow("Results", sub); cv2.waitKey(0)

    black = np.array([subtraction_parameter]) #lower bound
    white = np.array([255]) #upper bound (there is no upper bound)
    mask = cv2.inRange(sub, black, white) # true or false (white or black) if a pixel is within range
    if stops_huh:
        cv2.imshow("Results", mask); cv2.waitKey(0)

    # - reappy color to subtraction mask to do color analysis
    colorized_subtraction = cv2.bitwise_and(img, img, mask=mask) # only shows pixels within the mask range in test image for result
    if stops_huh: 
        cv2.imshow("Results", colorized_subtraction); cv2.waitKey(0)
    
    HSV_img = cv2.cvtColor(colorized_subtraction, cv2.COLOR_BGR2HSV)
    segmented_binary_img = cv2.inRange(HSV_img, lowHSV, highHSV)
    
    if stops_huh:
        cv2.imshow("Results", segmented_binary_img); cv2.waitKey(0)

    
    # - fill out the date with morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size_of_ellipse, size_of_ellipse))
    morphed_img = cv2.morphologyEx(segmented_binary_img, cv2.MORPH_CLOSE, kernel)
    if stops_huh:
        cv2.imshow("Results", morphed_img); cv2.waitKey(0)
    
    # at this point, the date should be the biggest foreground object in the image 
        
    
    # - remove outlying objects with contours # filter and show  
    contours, hierarchy = cv2.findContours(morphed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True) # get only largest contour

    mask = np.zeros(img.shape, np.uint8)
    cv2.drawContours(mask, np.array([contours[0]]), -1, (255,255,255), -1 )
    
    if stops_huh:
        cv2.imshow("Results", mask); cv2.waitKey(0)
            
    # # convert this RGB mask to a binary mask, don't really want to di inRange here... see how to fix    
    sub = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY) #makes subtraction grayscale to create a mask
    black = np.array([15]) #lower bound
    white = np.array([255]) #upper bound (there is no upper bound)
    mask = cv2.inRange(sub, black, white) # true or false (white or black) if a pixel is within range

    final = cv2.bitwise_and(img, img, mask=mask)
    if stops_huh:
        cv2.imshow("Results", final); cv2.waitKey(0)
    
    return final 

def main(stops_huh=True): 
    cv2.namedWindow("Results",cv2.WINDOW_NORMAL)
    cv2.namedWindow("Controls",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Controls",640,240)

    blank_img = cv2.resize(cv2.imread(".\\..\\ImageAssets\\Empty\\Empty1.jpg"), shape)
    image_paths = helper_functions.myimages('.\\..\\ImageAssets\\HighBlister\\')
    cv2.createTrackbar("Image","Controls",0,len(image_paths)-1,lambda _:_)
    
    
    while True: 
        img = cv2.imread(image_paths[cv2.getTrackbarPos("Image","Controls")])
        img = cv2.resize(img, shape) 
                
        final = get_me_a_date(img, blank_img, True)
        cv2.imshow("Results", final); cv2.waitKey(0)

        key = cv2.waitKey(500) # milliseconds, enough for it 
        if key == ord('q') or key == 27:
            break
    cv2.destroyAllWindows()


# try: 
main(stops_huh=True) 
# except Exception as e:
#     print(e)
