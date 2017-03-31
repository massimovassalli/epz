# EPZ 1.0
# DATA receiver running in a separate python thread.
# See skelDataRec.py for details

from .skelDataRec import SkelDataRec
from threading import Thread
from .epz import ENV

class DataRec(SkelDataRec, Thread):
    def __init__(self,device='ME', tag='TAG', environment=ENV):
        Thread.__init__(self)
        SkelDataRec.__init__(self, device=device, tag=tag, environment=environment)

    def setDataCallback(self,callback):
        self.setCallback(callback,1)

    def setValueCallback(self,callback):
        self.setCallback(callback,2)

    def setSaveCallback(self,callback):
        self.setCallback(callback,3)

    def setOverloadCallback(self,callback):
        self.setCallback(callback,4)

    def setCallback(self,callback,type = 1):
        if type == 1:
            self._callData = callback
            self.notify = True
        elif type== 2:
            self._callValue = callback
        elif type == 3:
            self._callSave = callback
        elif type == 4:
            self._callOverload = callback

    def _actondata(self,v):  #notify about a data pack received
        if self._callData is not None:
            self._callData(v)

    def _actOnValue(self,v):  #notify about a value received
        if self._callValue is not None:
            self._callValue(v)

    def _switchState(self,state):  #act on SAVE state change
        if self._callSave is not None:
            self._callSave(state)

    def _switchLoad(self,state):  #act on OVERLOAD state change
        if self._callOverload is not None:
            self._callOverload(state)