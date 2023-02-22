import plc_interface
from time import sleep
import cv2
import image_isolation as ii

import user_input
import datetime
import os

def myimages(imdir): # get all images in a directory 
    files = os.listdir(imdir)
    image_paths = list(
        map(lambda filename: imdir+filename, 
            filter(
                lambda filename: filename.endswith(('.jpg','.JPG')), files)
            )
        )
    return image_paths

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
    

    cam = cv2.VideoCapture(0)
    if cam is None or not cam.isOpened():
        print('Ensure the camera is connected and pointed at the sensor area. See manual for more details.')
        raise Exception('issue connecting camera')
    
    try:
        plcInterface = plc_interface.plcInterface()
    except Exception as e: 
        print('Interface with the machine cannot be established. Ensure the machine is plugged in, IP is configured, and PVI is activated. See manual for more details.')
        raise e # DISABLED FOR TESTING  
    
    try: 
        import db_Interface as dbi
    except Exception as e: 
        print('Interface with the Database cannot be established. Ensure the database is running and configured correctly. See manual for more details.')
        raise e 
        
        
    
    # -- input -- 
    input('Software startup complete, START the Machine now. Once it is fully on and conveyors are running, Press ENTER key to continue')
    # harvestDaySTR, barCode = user_input.get()  
    harvestDaySTR, barCode = '1111-11-11', 0
    measureDay = datetime.datetime.today().strftime('%Y-%m-%d')



    print()    
    input('Information about batch collected, Press ENTER key to continue')
    print() 

    # -- check if this file location already exists, give option to delete it, or to close the program 
    folder_name = harvestDaySTR+"_"+str(barCode)
    batch_folder_path = rf"C:\\DatesWorkspace\\DateIQP\\MyApp\\DateImages\\{(folder_name)}"
    if os.path.exists(batch_folder_path):
        # so it does exist 
        input_var = input(f'This batch file seems to already exist ({folder_name}). Press (ENTER) if you would like to delete it and overwrite. Otherwise, press (ANY KEY) for this program will terminate. (ENTER): ')
        if input_var == "": 
            image_paths_to_delete = myimages(batch_folder_path)
            # delete entries in db
            for path in image_paths_to_delete:
                dbi.dbDateDelete(path)
            # delete folder and images from file system
            import shutil
            shutil.rmtree(batch_folder_path)

        else: 
            print('shutting down because file path is duplicated and was told not to delete it. Please change batch number when re-running.')
            sys.exit() 

    # now that the path definitely does not exist, remake the empty one
    os.mkdir(batch_folder_path) 

    print()
    print('Place date batch on the starting conveyor and let the machine run. This script is currently watching for dates and will enter them into the SQL database. Once all the dates have gone through, press Ctrl+C to exit correctly.')
    print()

    print('Logs:')    
    # -- start watching for dates --
    index = 1
    while True: 
        # print('looped')

        status = plcInterface.wait_until_changed(plcInterface.Status)     

        if status==10: # date in the chamber  
            print('Date detected in sensor area.')
            sleep(0.75) # wait until date settled
            img = takepic(cam)
            print('Image taken.') 

            # - measure weight 
            newstatus = plcInterface.wait_until_changed(plcInterface.Status) 
            if status != newstatus: # numbers other than 9 or 10 mean that it has opened the door to clear 
            # if status!=10 and status!=9: # numbers other than 9 or 10 mean that it has opened the door to clear 
                print(f'Date {index} released.')
                sleep(0.1) # LAST_WEIGHT updates very soon after the doors open 
                weight = plcInterface.get_var(plcInterface.Weight)

                # take empty pic 
                empty_img = takepic(cam)
                
                #isolate img
                try: 
                    img = ii.get_me_a_date(img, empty_img)
                except IndexError as e: 
                    print('sensor tripped, but no date detected by the camera')
                    continue # end this iteration of the while loop 

                # store image               
                filepath = batch_folder_path + rf'\date_{str(index)}.jpg'
                cv2.imwrite(filepath, img)

                print('Weight recorded.')
                print('Image stored at: '+filepath)       

                row_info = {'imageAddress':filepath, 
                            'harvestDay':harvestDaySTR, 
                            'measureDay':measureDay, 
                            'barCode':barCode, 
                            'weight':weight }
                
                # send row to db 
                
                try: 
                    dbi.dbDateAdd( **row_info )
                    print('Entry to Database successful.')
                except Exception as e: 
                    print('unable to store into database: '+str(e))
                    
                index = index + 1 
                # display_img(img) 


if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt as e:
        print('exiting program correctly...') 
        import sys
        sys.exit()

    # - # testcases 
    # cam = cv2.VideoCapture(0)
    # while True: 
    #     takepic(cam, False)
    #     print('takepic')

    