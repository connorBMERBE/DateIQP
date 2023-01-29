import cv2
import numpy as np 

cap = cv2.VideoCapture(0) # 0 for each webcam connected to this device 

while True: 
    ret, frame = cap.read() # return is boolean that webcam is available to use, frame is video 
    
    frame = cv2.resize(frame,(800,800))
    
    width  = frame.shape[0]
    height = frame.shape[1]
    # width = int(cap.get(3))
    # height= int(cap.get(4)) 
    
    
    image = np.zeros(frame.shape, np.uint8) # black screen of whatever size
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_COUNTERCLOCKWISE) # top left
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_90_CLOCKWISE) # bottom left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # top right 
    image[height//2:, width//2:] = smaller_frame  # guess
    
    
    cv2.imshow('myframe', image)
    
    if cv2.waitKey(1) == ord('q'): # waits 1 millisecond, if "q" key pressed within that time, breaks look 
        break 
    
cap.release() 
cv2.destroyAllWindows() 

