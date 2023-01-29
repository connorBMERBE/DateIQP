import cv2
import numpy as np 

# cap = cv2.VideoCapture(0) # 0 for each webcam connected to this device 
def get_date_mask(img):
    
    # -- get data
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110, 50, 50]) # hsv 180, 255, 255
    upper_blue = np.array([130, 255, 255]) # hsv
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue) # true or false (white or black) if a pixel is within range

    result = cv2.bitwise_and(img, img, mask=mask) # comparing first 2 arguments (frame vs frame in this case) # where frame overlaps with itself having blue pixels 
    # -- 
    
    cv2.imshow("ImageName", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg")
get_date_mask(img)



# while True: 
#     ret, frame = cap.read() # return is boolean that webcam is available to use, frame is video 
        
#     # width = int(cap.get(3))
#     # height= int(cap.get(4))     
    
#     hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     lower_blue = np.array([110, 50, 50]) # hsv
#     upper_blue = np.array([130, 255, 255]) # hsv
#     mask = cv2.inRange(hsv_img, lower_blue, upper_blue) # true or false (white or black) if a pixel is within range

#     result = cv2.bitwise_and(frame, frame, mask=mask) # comparing first 2 arguments (frame vs frame in this case) # where frame overlaps with itself having blue pixels 

#     cv2.imshow('myframe', result) 
    
#     if cv2.waitKey(1) == ord('q'): # waits 1 millisecond, if "q" key pressed within that time, breaks look 
#         break 
    
# cap.release() 
# cv2.destroyAllWindows() 


# # def bgrtohsv(bgr):
# #     # [255, 0, 0]



