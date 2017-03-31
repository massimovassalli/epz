# EPZ 1.0
# Skeleton to create a DATA receiver object (counterpart of the DATA object)
# The class is designed to extend a threading class in standard python3 or a QtThread in Qt
# use the corresponding implementations, not this skeleton.

import zmq
import queue
from .epz import epzobject
from .data import DATA

class SkelDataRec(epzobject):

    def setZMQ(self):
        self._socket = None
        self.listen = True #Set to false to finish receiving
        self.decimate = 1 #if >1 decimate the received data array before sending for management
        self.chunk = 10000 #Size of data to take in memory before transferring to the program
        self.notifyLength = 1000 #Number of samples after which notify the last value
        self._tick = self.notifyLength
        self.x = []  #X data
        self.y = []  #Y data
        self.z = []  #Z data
        self._queue = []
        self._queue.append(queue.Queue())
        self._save = False
        self._overload = False
        self.notify = False #Set to true to notify and transfer the data array
        self.flushing = False #Set to True for a one shot flush of the in memory queue

        self._callData = None
        self._callValue = None
        self._callSave = None
        self._callOverload = None

        self._socket = self.context.socket(zmq.SUB)
        self._head = "{0}:{1}:".format(self.device, self.tag)
        self._socket.setsockopt_string(zmq.SUBSCRIBE, self._head)
        self._socket.connect("tcp://{0}:{1}".format(self.epserver, self.subport))

        self._stopit = DATA(device=self.device, tag=self.tag)

    def stop(self):
        self.listen = False
        self._stopit.send(0,0,0)

    @property
    def save(self):
        return self._save

    @save.setter
    def save(self, value):
        if self._save is not value:  #detect changes in the SAVE state of the data
            if not value:  #detect if save was switched off
                self._queue.append(queue.Queue())  #in case, append a new empty queue as the next active one
            self._switchState(value)  #inform the program that the state has been switched
        self._save = value

    @property
    def overload(self):
        return self._overload

    @overload.setter
    def overload(self, value):
        if self._overload is not value: #detect a change in the OVERLOAD state of the data
            self._switchLoad(value) #inform the program of the change in the state
        self._overload = value

    def flushMemory(self): #empty the queues memory
        self._queue = []
        self._queue.append(queue.Queue())

    def run(self):
        self.listen = True
        while self.listen:
            body = self._socket.recv_string()
            data = [float(x) for x in body[len(self._head):].split(':')] #NB: message is expected to be a list of numbers
            if self.flushing:
                self.flushMemory()
                self.flushing = False
            if (len(data)>=4) and (data[3] == 1.0): #Parameter 4 is the SAVE state, if present. Boolean so far
                self.save = True
            else:
                self.save = False

            if (len(data)>=5) and (data[4] == 1.0): #Parameter 5 is the OVERLOAD state, if present. Boolean so far
                self.overload = True
            else:
                self.overload = False
            if self.save and len(self._queue)>=1:
                self._queue[-1].put(data)

            self._tick -= 1
            if self._tick == 0:
                self._actOnValue(data)
                self._tick = self.notifyLength

            if self.notify:
                self.x.append(data[0])
                self.y.append(data[1])
                self.z.append(data[2])
                if len(self.x) >= self.chunk:
                    self._actondata([self.x[::self.decimate], self.y[::self.decimate], self.z[::self.decimate]])
                    self.x=[]
                    self.y=[]
                    self.z=[]
    def _actondata(self,v):  #notify about a data pack received
        pass

    def _actOnValue(self,v):  #notify about a value received
        pass

    def _switchState(self,state):  #act on SAVE state change
        pass

    def _switchLoad(self,state):  #act on OVERLOAD state change
        pass