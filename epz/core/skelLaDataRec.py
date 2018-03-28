# EPZ 1.0
# Skeleton to create a DATA receiver object (counterpart of the DATA object)
# The class is designed to extend a threading class in standard python3 or a QtThread in Qt
# use the corresponding implementations, not this skeleton.

import zmq
import queue
from .epz import epzobject
from .data import DATA

class SkelLaDataRec(epzobject):

    def setZMQ(self):
        self._socket = None
        self.listen = True #Set to false to finish receiving
        self.decimate = 1 #if >1 decimate the received data array before sending for management
        self.chunk = 10000 #Size of data to take in memory before transferring to the program
        self.tickLength = 1000 #Number of samples after which notify the last value
        self._tick = self.tickLength
        self._data = []  #DataList
        self._notify = False #Set to true to notify and transfer the data array

        self._callData = None
        self._callValue = None

        self._socket = self.context.socket(zmq.SUB)
        self._head = "{0}:{1}:".format(self.device, self.tag)
        self._socket.setsockopt_string(zmq.SUBSCRIBE, self._head)
        self._socket.connect("tcp://{0}:{1}".format(self.epserver, self.subport))

        self._stopit = DATA(device=self.device, tag=self.tag)


    @property
    def notify(self):

        return self._notify


    @notify.setter
    def notify(self,val):

        if not val:
            self.data = []
        self._notify = val


    def stop(self):
        self.listen = False
        self._stopit.send(0,0,0)


    def run(self):
        self.listen = True
        while self.listen:
            body = self._socket.recv_string()
            data = [float(x) for x in body[len(self._head):].split(':')] #NB: message is expected to be a list of numbers

            self._tick -= 1
            if self._tick == 0:
                self._actOnValue(data)
                self._tick = self.tickLength

            if self.notify:
                if len(self.data) == 0:
                    self.data = [[]]*len(data)
                for i in range(len(data)):
                    self.data[i].append(data[i])
                if len(self.data[0]) >= self.chunk:
                    self._actondata(self.data)
                    self.data = []


    def _actondata(self,v):  #notify about a data pack received
        pass

    def _actOnValue(self,v):  #notify about a value received
        pass