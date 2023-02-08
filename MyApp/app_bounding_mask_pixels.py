import cv2 as cv

# import argparse
max_value = 255
max_value_H = 360//2
low_H = 0
low_S = 0
low_V = 0
high_H = max_value_H
high_S = max_value
high_V = max_value

window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
window_controls_name = 'Controls'

low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'


# create windows 
cv.namedWindow(window_capture_name, cv.WINDOW_NORMAL)
cv.namedWindow(window_detection_name, cv.WINDOW_NORMAL)
cv.namedWindow(window_controls_name, cv.WINDOW_NORMAL)

cv.createTrackbar(low_H_name, window_controls_name , low_H, max_value_H, lambda _:_)
cv.createTrackbar(high_H_name, window_controls_name , high_H, max_value_H, lambda _:_)
cv.createTrackbar(low_S_name, window_controls_name , low_S, max_value, lambda _:_)
cv.createTrackbar(high_S_name, window_controls_name , high_S, max_value, lambda _:_)
cv.createTrackbar(low_V_name, window_controls_name , low_V, max_value, lambda _:_)
cv.createTrackbar(high_V_name, window_controls_name , high_V, max_value, lambda _:_)

# slider for images 
imagefilepaths = [".\\..\\ImageAssets\\subtraction\\full.JPG", ".\\..\\ImageAssets\\subtraction\\empty.JPG"]
cv.createTrackbar("image_selector", window_controls_name, 0, len(imagefilepaths)-1, lambda _:_)


# start running program 
while True:
    
    frame = cv.imread(imagefilepaths[cv.getTrackbarPos("image_selector", window_controls_name)])
    frame = cv.resize(frame, (800,800))

    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, 
                                 (cv.getTrackbarPos(low_H_name, window_controls_name), 
                                  cv.getTrackbarPos(low_S_name, window_controls_name), 
                                  cv.getTrackbarPos(low_V_name, window_controls_name)), 
                                 (cv.getTrackbarPos(high_H_name, window_controls_name), 
                                  cv.getTrackbarPos(high_S_name, window_controls_name), 
                                  cv.getTrackbarPos(high_V_name, window_controls_name)))


    try:
        contours, hierarchy = cv.findContours(frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        print(contours) 
        cv.drawContours(frame_threshold, contours, 0, (0,255,0), 3)
    except:
        pass

    cv.imshow(window_capture_name, frame)
    # cv.imshow(window_detection_name, frame_threshold)
    
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break
    
cv.destroyAllWindows()


