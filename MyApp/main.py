import interface 
from time import sleep
import cv2

import datetime 

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
    
    # -- setup camera and interfaces 
    
    try: 
        cam = cv2.VideoCapture(0)
    except Exception as e: 
        print('Ensure the camera is connected and pointed at the sensor area. See manual for more details.')
        raise e 
    
    try:
        plcInterface = interface.plcInterface()
    except Exception as e: 
        print('Interface with the machine cannot be established. Ensure the machine is plugged in, IP is configured, and PVI is activated. See manual for more details.')
        # raise e # DISABLED FOR TESTING  
    
    try: 
        dbInterface = None
    except Exception as e: 
        print('Interface with the Database cannot be established. Ensure the database is running and configured correctly. See manual for more details.')
        raise e 
        
        
    
    # -- input -- 
    import user_input
    harvestDay, barCode = user_input.get()    
    measureDay = datetime.datetime.today()


    print()    
    input('Information about batch collected, Press ENTER key to continue')
    print('Place date batch on the starting conveyor and let the machine run. This script is currently watching for dates and will enter them into the SQL database. Once all the dates have gone through, close this window.')
    print()

    
    # -- start watching for dates --
    index = 1
    while True: 
        # print('looped')

        status = plcInterface.wait_until_changed(plcInterface.Status)     

        if status==10: # date in the chamber  
            print('Date detected in sensor area.')
            sleep(0.2) # wait until date settled
            img = takepic(cam)
            print('Image taken.')

            # - measure weight 
            status = plcInterface.wait_until_changed(plcInterface.Status) 
            if status!=10 and status!=9: # numbers other than 9 or 10 mean that it has opened the door to clear 
                print(f'Date {index} released.')
                sleep(0.1) # LAST_WEIGHT updates very soon after the doors open 
                weight = plcInterface.get_var(plcInterface.Weight)

                # store image 
                folder_name = harvestDay.strftime('%Y-%m-%d')+"_"+barCode
                cv2.imwrite(folder_name+'/date_'+index+'.jpg', img)

                print('Weight and image recorded and stored.')              


                row_info = {'imageAddress':-1, 
                            'harvestDay':harvestDay.strftime('%Y-%m-%d'), 
                            'measureDay':measureDay.strftime('%Y-%m-%d'), 
                            'barCode':barCode, 
                            'weight':weight }
                
                # send row to db 

                print('Entry to Database successful.')

                index = index + 1 
                # display_img(img) 


if __name__ == "__main__":
    main()

    # - # testcases 
    # cam = cv2.VideoCapture(0)
    # while True: 
    #     takepic(cam, False)
    #     print('takepic')

    