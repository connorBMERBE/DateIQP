# https://github.com/hilch/Pvi.py

# import pvi 
import random 

class plcInterface():
    
    def __init__(self, ip="10.10.10.10"):
        pass

        # pviConnection = pvi.Connection() # start a Pvi connection        
        # line = pvi.Line( pviConnection.root, 'LNANSL', CD='LNANSL')  
        
        # self.BnR_PLC = pvi.Cpu( pvi.Device( line, 'TCP', CD='/IF=TcpIp' ), 'myArsim', CD='/IP='+ip ) 
        # self.CELL_01 = pvi.Task( self.BnR_PLC, 'CELL_01')
    
    # def get_weight(self): 
    #     IN_Cell_Sensor = pvi.Variable( self.CELL_01, 'IN_Cell_Sensor' )
    #     IN_Cell_Sensor_val = IN_Cell_Sensor.value
    #     IN_Cell_Sensor.kill() 
    #     return IN_Cell_Sensor_val

    # def get_sensor(self):
    #     LAST_WEIGHT = pvi.Variable( self.CELL_01, 'LAST_WEIGHT' )
    #     LAST_WEIGHT_val = LAST_WEIGHT.value
    #     LAST_WEIGHT.kill() 
    #     return LAST_WEIGHT_val

    # def get_weight_change_callback(self, afunc = print): 
    #     LAST_WEIGHT = pvi.Variable( CELL_01, 'LAST_WEIGHT' )
    #     LAST_WEIGHT.valueChanged = afunc
    #     LAST_WEIGHT.kill() 
        
    #     # - now it is important to call
    #     # while run:
    #     #     pviConnection.doEvents() # must be cyclically
        
    def get_weight(self):
        return random.choice(range(10))
    def get_sensor(self):
        return random.choice(range(2))
    
    
    def wait_until_changed(self, func):
        prev_weight = func()
        while True: 
            new_weight = func()
            if new_weight != prev_weight:
                return new_weight
            else: 
                prev_weight = new_weight


def main(): 

    # this loops for every date in a batch 
    while True: 
        myInterface = plcInterface() 
        
        # trip sensor 
        # new_value = myInterface.wait_until_changed(myInterface.get_sensor) 
        
        # take picture 
        
        # get weight
        # new_value = myInterface.wait_until_changed(myInterface.get_weight) 
        
        # -- 
        
        # calculate the quality with KNN 
        
        
        
        print(new_value)


    
    
if __name__ == "__main__":
    main() 
