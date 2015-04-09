"""
Gloabl EPZ library example with terminal output
Here all components are started in the same machine from the same process
but each of it can be started in a different machine
"""
# import epz library for Python 3
import epz3 as epz

# set the IP address of the FW device
epz.EPSERVER = '127.0.0.1'

import time # just to slow down the execution

# instantiate the forwarder and start
fw = epz.Forwarder()
# note: fw.daemon is internally set to False, to avoid closure of the
# forwarding thread just at the end of the script. Here we aim that
# behavior so ...
fw.daemon = True
fw.start()
print ("FW started")
time.sleep(2)

# setting up an hardware device
dev = epz.Device('TEST')
# add two parameters
# so add a name, a default value and a fake callback
dev.append(epz.HWparameter('gain',7.0))
# start the device
dev.start()
# Ah, I saw parameterS, I forgot one, but I can add it
# even if the device is already running
# first inherits the HWparameter to change the standard update behavior

class MyHw(epz.HWparameter):
    def update(self,v):
        if v > 200:
            return False
        return True

dev.append(MyHw('offset',4))  # NB: using an int to init the parameter will force a cast to int for each next assignment
print ("device configured and ready to interact")
time.sleep(2)


# play with the device from a consumer
# create two objects able to interact with their HW counterpart
# for device 'TEST' parameter 'gain'
gain = epz.Parameter('TEST', 'gain')
# gain is not yet in the game, start it!
gain.start()
# the same for device 'TEST' parameter 'offset'
offset = epz.Parameter('TEST','offset')
offset.start()
print ('Consumer-side parameters GAIN and OFFSET created and started')
time.sleep(1)

print ("Now starting to play\n")
time.sleep(2)

print ('GAIN: {0} OFFSET: {1}'.format(gain.value,offset.value))  # Both parameters should be None = never queried
time.sleep(2)
print ('Query for the current value ...')
print ('The hardware value for gain and offset are now {0} - {1}'.format(dev.hw['gain'].value,dev.hw['offset'].value))
gain.query()  # ask the device to tell the current value
offset.query()
time.sleep(2)
print ('The consumer gain and offset are now: {0} - {1}'.format(gain.value,offset.value))  # now it should update to the hardware value
time.sleep(2)
print ("Now we would like to set the value from the client to 27.5 for both")
gain.value = 27.5  # Now set the value
offset.value = 27.5
time.sleep(2)
print ("I verify")
print ('SW GAIN: {0} OFFSET: {1} '.format(gain.value,offset.value))
print ('HW GAIN: {0} OFFSET: {1}'.format(dev.hw['gain'].value,dev.hw['offset'].value))
time.sleep(2)
print ("Now again we would like to set the value from the client to 142.1 that is out of range for gain ")
gain.value = 142.1  # Now set the value
offset.value = 142.1  # Now set the value
time.sleep(2)
print ("I verify")
print ('SW GAIN: {0} OFFSET: {1} '.format(gain.value,offset.value))
print ('HW GAIN: {0} OFFSET: {1}'.format(dev.hw['gain'].value,dev.hw['offset'].value))