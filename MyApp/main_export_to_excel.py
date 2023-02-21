import pandas as pd
import sql.connector as sql 

def dbViewFiltered(): 

    cursor.execute(f'')    


# harvestDaySTRING = "2022-02-20"
# barcode = "123456789"

print("You are running a script that will download a filtered section of the MySQL database running on this computer.")

import user_input.py

harvestDaySTRING, barCode = user_input.get()

cursor.execite(f"SELECT * FROM dates WHERE harvestDay = {harvestDaySTRING} AND barCode = {barCode}")

location = {'imageAddress':-1, 
            'harvestDay':harvestDay.strftime('%Y-%m-%d'), 
            'measureDay':measureDay.strftime('%Y-%m-%d'), 
            'barCode':barCode, 
            'weight':weight }




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