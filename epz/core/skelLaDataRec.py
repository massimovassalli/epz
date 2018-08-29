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
        self.actionCount = 0
        self.chunk = 10000 #Size of data to take in memory before transferring to the program
        self._data = []  #DataList
        self._notify = False #Set to true to notify and transfer the data array
        self._oldNotify = False
        self._acting = False
        self._oldActing = False
        self._paused = False

        self._callNotify = None
        self._callData = None

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
            self._data = []
        self._notify = val


    @property
    def act(self):

        return self._acting


    @act.setter
    def act(self,value):

        self._acting = value

    def stop(self):
        self.listen = False
        self._stopit.send(0,0,0)


    def pause(self):

        self._paused = not self._paused

        if self._paused:
            if self.notify:
                self._oldNotify = self._notify
                self.notify = not self._paused
            if self.act:
                self._oldActing = self._acting
                self.act = not self._paused
        else:
            if self._oldNotify:
                self._oldNotify = self.notify
                self.notify = not self._paused
            if self._oldActing:
                self._oldActing = self.act
                self.act = not self._paused


    def run(self):
        self.listen = True
        while self.listen:
            body = self._socket.recv_string()
            data = [float(x) for x in body[len(self._head):].split(':')] #NB: message is expected to be a list of numbers
            if len(self._data) != 0:
                if len(data) != len(self._data):
                    continue
            if self.act:
                self.actionCount += 1
                if self.actionCount == self.decimate:
                    self._actOnData(data)
                    self.actionCount = 0

            if self.notify:
                if len(self._data) == 0:
                    self._data = [[]]*len(data)
                for i in range(len(data)):
                    self._data[i].append(data[i])
                if len(self._data[0]) >= self.chunk:
                    self._notification(self._data[::self.decimate])
                    self._data = []


    def _notification(self,v):  #notify about a data pack received
        pass


    def _actOnData(self,v):
        pass