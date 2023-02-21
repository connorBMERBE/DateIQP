import datetime 

def get():
    while True: 
        entry = input('For this batch, enter the Day Harvested in (YYYY-MM-DD) format: ')
        year, month, day = map(int, entry.split('-'))
        harvestDay = datetime.date(year, month, day)

        print('Is this correct? '+harvestDay.strftime('%Y-%m-%d'))
        x = input('You will not be able to change this while the script is running. Confirm by Re-entering Day Harvested (YYYY-MM-DD): ')
        if x == harvestDay:
            break

    while True: 
        barCode = int(input("For this batch, enter the Tree Barcode Number: "))
        print('Is this correct? '+str(barCode))
        x = input('You will not be able to change this while the script is running. Confirm by Re-entering Tree Barcode Number: ')
        if x == barCode:
            break

    return harvestDay.strftime('%Y-%m-%d'), barCode 


# folder_name = harvestDay+"_"+barCode

