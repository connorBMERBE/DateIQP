import interface 
from time import sleep
import cv2

def display_img(img):
    while True: 
        cv2.imshow('test', img)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

def takepic(cam, show=False): 
    ret, frame = cam.read()

    if show: 
        display_img(frame)
    
    return frame 

def main(): 
    cam = cv2.VideoCapture(0)
    myInterface = interface.plcInterface()
    print('startup complete')

    while True: 
        print('looped')

        # weight = myInterface.get_var(myInterface.Weight)     
        # print('original weight',weight) 

        status = myInterface.wait_until_changed(myInterface.Status)     
        # print(status)

        if status==10: # date in the chamber  
            sleep(0.2) # wait until date settled
            img = takepic(cam)

            # - measure weight 
            status = myInterface.wait_until_changed(myInterface.Status) 
            if status!=10 and status!=9: # numbers other than 9 or 10 mean that it has opened the door to clear 
                sleep(0.1) # LAST_WEIGHT updates very soon after the doors open 
                weight = myInterface.get_var(myInterface.Weight)
                # weight = myInterface.wait_until_changed(myInterface.Weight)  
                # print('new weight ', weight) 

                row_info = {'index':-1,'weight':weight,'img':img}
                print(row_info)

                display_img(img) 

                # send to db 
        
            

if __name__ == "__main__":
    main()

    # - # testcases 
    # cam = cv2.VideoCapture(0)
    # while True: 
    #     takepic(cam, False)
    #     print('takepic')

    