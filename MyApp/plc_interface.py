# https://github.com/hilch/Pvi.py
import pvi 

class plcInterface():
    
    def __init__(self, ip="10.10.10.10"):
        self.pviConnection = pvi.Connection() # start a Pvi connection        
        line = pvi.Line( self.pviConnection.root, 'LNANSL', CD='LNANSL')  
        
        device = pvi.Device( line, 'TCP', CD='/IF=TcpIp' )
        self.BnR_PLC = pvi.Cpu( device, 'myArsim', CD='/IP='+ip ) 
        self.CELL_01 = pvi.Task( self.BnR_PLC, 'CELL_01')
        
        self.Sensor = pvi.Variable( self.CELL_01, 'IN_Cell_Sensor' )
        self.Weight = pvi.Variable( self.CELL_01, 'LAST_WEIGHT' )
        self.Status = pvi.Variable( self.CELL_01, 'Weight_State' ) 
        
        # test connection, will raise error if it cannot get a status  
        # self.get_var(self.Status) 
    
    def get_var(self, myvar): 
        # just get the var, with doEvents to update the value. impliment into wait_until_changed
        
        for i in range(3): 
            
            try: 
                self.pviConnection.doEvents() # must be cyclically
                if myvar.readable: 
                    return myvar.value 
            except pvi.Error.PviError as er: 
                print('retrying pvi connection issue')
                # e = er

        # e = Exception('exception in pvi connection, see manual for details')        
        # raise e # raise the error if it doesnt work after 2 
        
          
    def wait_until_changed(self, myvar):

        prev_weight = self.get_var(myvar)

        while True: # wait until myvar is readable and it has changed
            new_weight = self.get_var(myvar) 
            if new_weight != prev_weight:
                return new_weight
  
if __name__ == "__main__":
    myInterface = plcInterface()
    print('startup complete')

    # continuously prints updated versions of variable
    while True: 
        new_value = myInterface.wait_until_changed(myInterface.Status)     
        print(new_value)
    

