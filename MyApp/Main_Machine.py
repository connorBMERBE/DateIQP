from time import sleep
import cv2

import main_classification_script
import main_export_to_excel as mete

import user_input
import datetime
import os
import sys

debug = False


# -- make sure equipment is set up correctly 
try:
    import plc_interface
    plcInterface = plc_interface.plcInterface()
except Exception as e:     
    if debug: 
        raise e # DISABLED FOR TESTING  
    else: 
        print('Interface with the machine cannot be established. Ensure the machine is plugged in, IP is configured, and PVI is activated. See manual for more details.')
        raise e

try: 
    import db_Interface as dbi
except Exception as e: 
    if debug: 
        raise e # DISABLED FOR TESTING  
    else: 
        print('Interface with the Database cannot be established. Ensure the database is running and configured correctly. See manual for more details.')
        raise e 
    
cam = cv2.VideoCapture(0)
if cam is None or not cam.isOpened():
    print('Ensure the camera is connected and pointed at the sensor area. See manual for more details.')
    raise Exception('issue connecting camera')

# cam, plcInterface, dbi = ensure_equipment_setup()



# -- helper functions 
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



# -- main functions 
def the_main_logger(harvestDaySTR, barCode, measureDay): 
    
    # -- check if this file location already exists, give option to delete it, or to close the program 
    folder_name = harvestDaySTR+"_"+str(barCode)
    batch_folder_path = rf"C:\\DatesWorkspace\\DateIQP\\MyApp\\DateImages\\{(folder_name)}\\"
    if os.path.exists(batch_folder_path):
        # so it does exist 
        print(f'This harvestday_barcode file seems to already exist ({folder_name}). You must press (ENTER) if you would like to delete previous entries and continue. Otherwise, enter (ANY KEY) for this program will terminate.')
        input_var = input('(ENTER): ')
        print()
        if input_var == "": 
            image_paths_to_delete = myimages(batch_folder_path)
            # delete entries in db
            for path in image_paths_to_delete:
                dbi.dbDateDelete(rf'{path}')
            # delete folder and images from file system
            import shutil
            shutil.rmtree(batch_folder_path)

        else: 
            raise Exception('Shutting down because file path is duplicated and was instructed not to delete it. Please change (Barcode Number) or (Harvest Day) when re-running.')
            
            

    # now that the path definitely does not exist, remake the empty one
    os.mkdir(batch_folder_path) 

    # startup! 
    print()
    print('Place date batch on the starting conveyor and let the machine run. This script is currently watching for dates and will enter them into the SQL database. Once all the dates have gone through, press Ctrl+C (ONLY ONCE!) to continue to classification.')
    print() 
    
    # take empty pic 
    empty_img = takepic(cam)
    cv2.imwrite("C:\DatesWorkspace\DateIQP\MyApp\DateImages\EmptyImage.jpg", empty_img)

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
                

                # store image               
                filepath = batch_folder_path + rf'date_{str(index)}.jpg'
                cv2.imwrite(filepath, img)

                print('Weight recorded.')
                print('Image stored at: ' + rf"{filepath}")       

                row_info = {'imageAddress':rf"{filepath}", 
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
        print()

def main():
    try: 
        # -- input -- 
        print('Software startup complete, START the machine as explained in the manual.')
        input('Once it is fully on and conveyors are running, Press ENTER key to continue')
        
        harvestDaySTR, barCode = user_input.get()
        measureDay = datetime.datetime.today().strftime('%Y-%m-%d')

        print()    
        input('Information about batch collected, Press ENTER key to continue')
        print() 
        # -- call logger 
        the_main_logger(harvestDaySTR, barCode, measureDay) # this has stored the images and the database entries 
    except KeyboardInterrupt:
        
        while True: 
            try: 
                print('You are now moving to the classification section of the program.')
                input('Press (ENTER) to start: ')
                print()
            except KeyboardInterrupt: # this is here in case user hits CTRL+C more than once 
                print('Do not press CTRL+C after this point! This will exit the program!')
                print()
    
                continue # restart for loop 

        # -- they have hit enter and are moving on to the classification script
        main_classification_script.main(harvestDaySTR, barCode, dbi, mete) 

        print('exiting program correctly...') 






if __name__ == "__main__":
    try: 
        main()
    except Exception as e: 
        print(e)
        input("ran into error, Press Enter to close correctly: ")
   