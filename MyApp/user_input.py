import datetime 

def get():
    while True: 
        print('For this batch, enter the Day Harvested.')
        
        entry = input('Day Harvested (YYYY-MM-DD): ')
        print()
        
        try: 
            year, month, day = map(int, entry.split('-'))
            harvestDay = datetime.date(year, month, day)
        except: 
            # not a correct date
            print('\nThe day you entered is not a calendar day. \nPlease try again.\n')
            continue
            

        print('You input ('+harvestDay.strftime('%Y-%m-%d') + '), Is this correct? You will not be able to change this while the script is running. Confirm by Re-entering Day Harvested.')
        

        x = input('Day Harvested (YYYY-MM-DD): ')
        print()
        
        if x == harvestDay.strftime('%Y-%m-%d'):
            break
        else:
            print('\nThe days you entered were not the same. \nPlease try again.\n')

    while True: 
        print('For this batch, enter the Tree Barcode Number.')
        barCode = input("Tree Barcode Number: ")
        print() 
        
        if barCode.isdigit():
            barCode = int(barCode)
        else: 
            print('\nThe Barcode you entered was not an integer. \nPlease try again.\n')
            continue
        
        print('You input ('+ str(barCode) + '), Is this correct? You will not be able to change this while the script is running. Confirm by Re-entering Tree Barcode.')

        x = input('Tree Barcode Number: ')
        print()
        
        if int(x) == barCode:
            break
        else:
            print('\nThe Tree Barcode Numbers you entered were not the same. \nPlease try again.\n')

    return harvestDay.strftime('%Y-%m-%d'), barCode 


# folder_name = harvestDay+"_"+barCode

if __name__ == "__main__":
    get()