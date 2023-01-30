#imports
import numpy as np
import cv2

# Load in the images from the file:
control=cv2.imread(".\\ImageAssets\\blank.jpg") #blank image of tray (control variable)
test=cv2.imread(".\\ImageAssets\\date.jpg") #test image of date on tray

#Creating the mask:
sub=cv2.subtract(control,test) #subtraction of empty tray from date on tray to isolate date
sub = cv2.resize(sub, (800,800)) #resizes image to a readable scale
test = cv2.resize(test, (800, 800)) #resizes image to a readable scale
sub = cv2.cvtColor(sub,cv2.COLOR_BGR2GRAY) #makes subtraction grayscale to create a mask
black = np.array([15]) #lower bound
white = np.array([255]) #upper bound (there is no upper bound)
mask = cv2.inRange(sub, black, white) # true or false (white or black) if a pixel is within range
result = cv2.bitwise_and(test, test, mask=mask) # only shows pixels within the mask range in test image for result

#Displaying the image:
cv2.imshow("Subtraction Mask", result) #shows image
cv2.waitKey(0)
cv2.destroyAllWindows()
