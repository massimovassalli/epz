# EPZ 1.0
# DATA receiver running in a separate python thread.
# See skelDataRec.py for details

from .skelLaDataRec import SkelLaDataRec
from threading import Thread
from .epz import ENV

class LaDataRec(SkelLaDataRec, Thread):
    def __init__(self,device='ME', tag='TAG', environment=ENV):
        Thread.__init__(self)
        SkelLaDataRec.__init__(self, device=device, tag=tag, environment=environment)


    def setDataCallback(self,callback):
        self.setCallback(callback,1)


    def setNotifyCallback(self,callback):
        self.setCallback(callback,2)


    def setCallback(self,callback,type = 1):
        if type == 1:
            self._callData = callback
            self.notify = True
        elif type== 2:
            self._callNotify = callback


    def _actOnData(self,v):  #notify about a data pack received
        if self._callData is not None:
            self._callData(v)


    def _notification(self,v):  #notify about a value received
        if self._callNotify is not None:
            self._callNotify(v)
