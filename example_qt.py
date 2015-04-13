"""
Gloabl EPZ library example with graphical output
Here all components are started in the same machine from the same process
but each of it can be started in a different machine
"""
# import epz library for Python 3
import epz3 as epz
import time # just to slow down sometime the execution

# set the IP address and ports (why not ?) of the FW device
epz.EPSERVER = '127.0.0.1'
epz.PUBPORT = 4900
epz.SUBPORT = 4910

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
# add one HW parameter 'gain' and one HW signal 'sin'
# so add a name and a default value (remember, the type of the init value will be used to cast any next value)
dev.append(epz.HWparameter('gain',7.0))

# start the device
dev.start()

# Create a signal that generates a sin wave + noise with amplitude given by the parameter 'gain'
# Do it by inheriting HWsignal and overloading the acquire function
import numpy as np
class MySignal(epz.HWsignal):
    def acquire(self):
        import numpy.random as npr
        t = time.clock()
        n = npr.random()
        signal = self.device.hw['gain'].value * np.sin(2*np.pi*t/1.0)+n
        return signal

# Remember to add also this signal to the game, device will start all background threads
dev.append(MySignal('sin'))
print ("device configured and ready to interact")
time.sleep(2)

# Now create a qt graph window
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

win = pg.GraphicsWindow(title = "EpsilonPi Qt test")
win.resize(1200,300)
grafo = win.addPlot(title = "Connection to EP device")
CHUNK = 2000
xmain = np.linspace(0,2*np.pi,CHUNK)
data = []
for i in range(CHUNK):
    data.append(np.random.normal())
curve = grafo.plot(np.linspace(0,2*np.pi,len(data)),data, title="Simplest possible plotting example",pen='y')
grafo.disableAutoRange()
grafo.setRange(yRange=(-11.0,11.0))

# Now we have the window ready to be shown; go defining the Consumer stuff

# Parameter for device 'TEST' parameter 'gain'
gain = epz.Parameter('TEST', 'gain')
# gain is not yet in the game, start it!
gain.start()
# Signal corresponding to the hardware-generated 'sin' wave
sig = epz.Signal('TEST','sin')
sig.start()
p = epz.Parameter('TEST','gain')
p.start()
p.query()

# The game will be done by two timers OVO is polling for changes in the data to rewrite the graph
def plotUpdate():
    hm = sig.queue.qsize()

    for i in range(min(hm,CHUNK)):
        dg = sig.queue.get()
        data.append(dg)
    d = data[-CHUNK:]
    curve.setData(xmain,np.array(d))

ovo = QtCore.QTimer()
ovo.timeout.connect(plotUpdate)
ovo.setInterval(1000.0/50.0)
ovo.start()

# Function changethings is a sequence of actions triggered each 3s by the timer action

q = 0
def changethings():
    global q
    q += 1

    if q < 10:
        n = 10.0*np.random.random()
        print("New wanted gain {0}".format(n))
        p.value = n
    elif q == 10:
        print("Switching OFF for 3 secs")
        sig.value = -1
    elif q == 11:
        print("And now going on at fixed amplitude")
        sig.value = 1
        p.value = 7.5
    elif q == 12:
        print("I'll start to decimate the signal")
    elif q == 25:
        print("sending the kill signal")
        epz.killdevice('TEST')
    elif q > 12 and q<= 25:
        decimations = [1,5,10,20,40,100]
        d = decimations[(q-13)%len(decimations)]
        print("Decimate of {0}".format(d))
        sig.value = d

action = QtCore.QTimer()
action.timeout.connect(changethings)
action.setInterval(3000)
action.start()

QtGui.QApplication.instance().exec_()