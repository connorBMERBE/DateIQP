# simple2.py
# An example that shows the application possibilities of https://github.com/hilch/Pvi.py
#
# PLC counterpart is B&R's 'coffee machine' running on ArSim 
# as provided with Automation Studio 4.1.17.113 (which
# can be downloaded free of charge from https://www.br-automation.com)
#
# this simple example just registers a variable for reading and another
# for writing. In fact we switch on the 'coffee machine' and watch its temperature ...
#


from time import sleep
from pvi import *

pviConnection = Connection() # start a Pvi connection

# all PVI objects must be registered hierarchically
# line ANSL is the 'modern' way to access PLC variables
# (compared to the older INA2000 line)
#
line = Line( pviConnection.root, 'LNANSL', CD='LNANSL')
device = Device( line, 'TCP', CD='/IF=TcpIp' )
cpu = Cpu( device, 'myArsim', CD='/IP=10.10.10.10' )
task1 = Task( cpu, 'CELL_01')
# we register the variable containing the temperature 
IN_Cell_Sensor = Variable( task1, 'IN_Cell_Sensor' )
# we register a callback to get temperature value
# IN_Cell_Sensor.valueChanged = lambda value : print( f'\IN_Cell_Sensor = {value}' )

run = True
# warmUp = False
# coolDown = False


# def cpuErrorChanged( error : int ):
#     global run

#     if error != 0:
#         raise PviError(error)

# cpu.errorChanged = cpuErrorChanged


while run:
    pviConnection.doEvents() # must be cyclically called

    if IN_Cell_Sensor.readable:
        print (IN_Cell_Sensor.value) 
        pass
    else:
        print("HI")
        

        # if temperature.value < 25 and not warmUp and not coolDown:
        #     switch.value = 1 # switch on machine
        #     warmUp = True
        #     coolDown = False
        #     print('warming up...')
        # elif temperature.value > 70 and warmUp:
        #     warmUp = False
        #     coolDown = True
        #     switch.value = False # switch off
        #     print('\ncooling down...')        
        # if coolDown and not warmUp and temperature.value < 25:
        #     print("\nit's cool guys !")
        #     run = False # exit the loop
        # else:
        #     sleep(0.1)





