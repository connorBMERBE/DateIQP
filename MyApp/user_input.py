import datetime 

def get():
    while True: 
        entry = input('For this batch, enter the Day Harvested in (YYYY-MM-DD) format: ')
        year, month, day = map(int, entry.split('-'))
        harvestDay = datetime.date(year, month, day)

        print('Is this correct? '+harvestDay.strftime('%Y-%m-%d'))
        x = input('You will not be able to change this while the script is running. Confirm by Re-entering Day Harvested (YYYY-MM-DD): ')
        if x == harvestDay.strftime('%Y-%m-%d'):
            break
        else:
            print('\nThe days you entered were not the same. \nPlease try again.\n')

    while True: 
        barCode = int(input("For this batch, enter the Tree Barcode Number: "))
        print('Is this correct? '+str(barCode))
        x = input('You will not be able to change this while the script is running. Confirm by Re-entering Tree Barcode Number: ')
        if x == str(barCode):
            break
        else:
            print('\nThe Tree Barcode Numbers you entered were not the same. \nPlease try again.\n')

    return harvestDay.strftime('%Y-%m-%d'), barCode 


# folder_name = harvestDay+"_"+barCode

