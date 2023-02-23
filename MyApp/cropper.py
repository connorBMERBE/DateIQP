import main_logger as ml
#this is a testing function to make sure the camera is looking at as little of the image as possible to get the entire date
cam = ml.cv2.VideoCapture(0)
img = ml.takepic(cam)
#in [x:y, a:b]:
#   x = low bound for height from top of image
#   y = high bound for height from top of image
#   a = low bound for width from left of image
#   b = high bound for width from left of image
img = img[25:385, 200:600]
while True: 
        ml.cv2.imshow('test', img)
        if ml.cv2.waitKey(1) == ord('q'):
            ml.cv2.destroyAllWindows()
            break