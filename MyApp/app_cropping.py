# https://stackoverflow.com/questions/15341538/numpy-opencv-2-how-do-i-crop-non-rectangular-region

import cv2
import numpy as np

# original image
# -1 loads as-is so if it will be 3 or 4 channel as the original
image = cv2.imread(".\\..\\ImageAssets\\subtraction\\full.JPG", -1)
# mask defaulting to black for 3-channel and transparent for 4-channel
# (of course replace corners with yours)
mask = np.zeros(image.shape, dtype=np.uint8)
roi_corners = np.array([[(0,0), (800,800), (0,800), (800, 0), (40,80)]], dtype=np.int32)
# fill the ROI so it doesn't get wiped out when the mask is applied
channel_count = image.shape[2]  # i.e. 3 or 4 depending on your image
ignore_mask_color = (255,)*channel_count
cv2.fillPoly(mask, roi_corners, ignore_mask_color)
# from Masterfool: use cv2.fillConvexPoly if you know it's convex

# apply the mask
masked_image = cv2.bitwise_and(image, mask)

#Displaying the image:
cv2.imshow("Subtraction Mask", masked_image) #shows image
cv2.waitKey(0)
cv2.destroyAllWindows()

