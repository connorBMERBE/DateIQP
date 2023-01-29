import cv2
import numpy as np
  
# Let's load a simple image with 3 black squares
image = cv2.imread('C:\\Workspace\\Projects\\DatesProject\\DateIQP\\tutorials\\assets\\blistered_date.jpg')
image = cv2.resize(image, (800,800))

image = cv2.GaussianBlur(image, (5,5), 0) 

  
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Find Canny edges
edges = cv2.Canny(gray, 100, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
  
print("Number of Contours found = " + str(len(contours)))
  

contours = sorted(contours, key=cv2.contourArea, reverse= True)
# contours = contours[0:1]

print(contours[0])

for c in contours: 
    
    
    # Draw all contours
    # -1 signifies drawing all contours
    cv2.drawContours(image, [c], -1, (0, 255, 0), 3)
  
    cv2.imshow('Contours', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
