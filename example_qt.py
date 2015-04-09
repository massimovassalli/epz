"""
Gloabl EPZ library example with terminal output
Here all components are started in the same machine from the same process
but each of it can be started in a different machine
"""
# import epz library for Python 3
import epz3 as epz

# set the IP address of the FW device
epz.EPSERVER = '127.0.0.1'
epz.PUBPORT = 4900
epz.SUBPORT = 4910

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
# add one HW parameter and one HW signal using the parameter
# so add a name and a default value (remember, the type of the init value will be used to cast any next value)
dev.append(epz.HWparameter('gain',7.0))
# start the device
dev.start()

# first inherits the HWparameter to change the standard update behavior
import numpy as np
class MySignal(epz.HWsignal):
    def acquire(self):
        import numpy.random as npr
        t = time.clock()
        n = npr.random()
        signal = self.device.hw['gain'].value * np.sin(2*np.pi*t/1.0)+n
        return signal

dev.append(MySignal('sin'))
print ("device configured and ready to interact")

time.sleep(2)



# play with the device from a consumer
# create two objects able to interact with their HW counterpart
# for device 'TEST' parameter 'gain'
gain = epz.Parameter('TEST', 'gain')
# gain is not yet in the game, start it!
gain.start()
# the same for device 'TEST' parameter 'offset'


from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg

win = pg.GraphicsWindow(title = "EpsilonPi Qt test")
win.resize(500,300)
grafo = win.addPlot(title = "Connection to EP device")
CHUNK = 2000
xmain = np.linspace(0,2*np.pi,CHUNK)
data = []
for i in range(CHUNK):
    data.append(np.random.normal())
curve = grafo.plot(np.linspace(0,2*np.pi,len(data)),data, title="Simplest possible plotting example",pen='y')
grafo.enableAutoRange('x', False)

sig = epz.Signal('TEST','sin')
sig.setType(1)
sig.start()
sig.query()

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

p = epz.Parameter('TEST','gain')
p.start()
p.query()

q = 0
def changeThings():
    global q
    q += 1
    if q % 3 == 0:
        print("Switching")
        if sig.value == -1:
            sig.value = 1
        else:
            sig.value = -1
    else:
        n = 10.0*np.random.random()
        print("New wanted gain {0}".format(n))
        p.value = n

action = QtCore.QTimer()
action.timeout.connect(changeThings)
action.setInterval(3000)
action.start()

QtGui.QApplication.instance().exec_()