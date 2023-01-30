# importing the module
import cv2

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):


    if event == cv2.EVENT_LBUTTONDOWN: # checking for left mouse clicks

        print(x, ' ', y)
        cv2.putText(img, str(x) + ',' + str(y), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    if event==cv2.EVENT_RBUTTONDOWN:

        frame_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # print(x, ' ', y)
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        
        print('h: ',b,' s: ',g,' v: ',r)
        # print('b: ',b,' g: ',g,' r: ',r)
        cv2.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2) 
        cv2.imshow('image', img) 
        
        

# driver function
if __name__=="__main__":

    # while True: 
    img = cv2.imread("DateIQP\\ImageAssets\\blistered_date.JPG")
    img = cv2.resize(img, (800,800))
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)

    key = cv2.waitKey(30)
    # if key == ord('q') or key == 27:
        # break

    cv2.destroyAllWindows()
