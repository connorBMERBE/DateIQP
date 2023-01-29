import cv2
import numpy as np

hsv_img = cv2.cvtColor(np.uint8([[[0,0,1]]]), cv2.COLOR_BGR2HSV)

print(hsv_img) 

