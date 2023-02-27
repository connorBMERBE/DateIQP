# Standard imports
import cv2
import numpy as np;
 
# Read image
im = cv2.imread("DateIQP\\ImageAssets\\normal_date.JPG") # cv2.IMREAD_GRAYSCALE
im = cv2.resize(im, (800,800))




# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# # Change thresholds
# params.minThreshold = 10;
# params.maxThreshold = 200;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 4000
params.maxArea = 800*800;

# params.minDistBetweenBlobs = 2
 
# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1
 
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
 
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01





# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create(params)
 
# Detect blobs.
keypoints = detector.detect(im)
 
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)

