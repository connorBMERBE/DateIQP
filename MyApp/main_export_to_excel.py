import pandas as pd
import user_input
import db_Interface as dbi

def main():
    print("You are running a script that will download a filtered section of the MySQL database running on this computer.")
    
    harvestDaySTRING, barCode = user_input.get()
    # harvestDaySTRING = "2022-02-20"
    # barcode = "123456789"
    rows_info = dbi.getFilteredDatesData(harvestDaySTRING, barCode) # array of rows 
    # rows_info = [[1,2,3,4, 5,6,7,8,9,10,11,12],[11,12,13,14, 15,16,17,18,19,20,21,22]]

    headers = ['imageAddress', 
               'measureDay',
               'barCode',
               'weight',
               
               'readyOrJuicy',
               'moist',
               'yellow',
               'halfFirm',
               'form',
               'blistered',
               'skippedAStage',
               'dry']
    
    DF = pd.DataFrame(data = rows_info, columns = headers)
    location = 'output.xlsx'
    DF.to_excel(location)

    print('Selected part of the database has been saved in: '+location)


if __name__ == "__main__":
    main() 





# imageAddress VARCHAR(255) NOT NULL, #image location
# harvestDay DATE NOT NULL, #day of tree harvest, format YYYY-MM-DD
# measureDay DATE NOT NULL, #day of date classification, format YYYY-MM-DD
# barCode INT(6) UNSIGNED NOT NULL, #tree identifier
# weight DOUBLE(3,1) NOT NULL,

# readyOrJuicy BOOLEAN,
# moist BOOLEAN,
# yellow BOOLEAN,
# halfFirm BOOLEAN,
# firm BOOLEAN, #(AKA smooth)
# blistered BOOLEAN,
# skippedAStage BOOLEAN,
# dry BOOLEAN,

# CONSTRAINT Dates_PK PRIMARY KEY (imageAddress)    		