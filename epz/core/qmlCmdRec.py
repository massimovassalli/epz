# EPZ 2.1
# CMD receiver running in a separate Qt thread.
# Specialized Qt signals are emitted upon data reception; connect them to get them alive
# See skelCmdRec.py for details

from .skelCmdRec import SkelCmdRec
from .epz import ENV

from PySide2.QtCore import QThread, Signal, Slot


class QMLCMDREC(SkelCmdRec, QThread):

    respReceived = Signal(str, name='respReceived')
    respReceivedL = Signal(list,name='respReceivedL')
    timedOut = Signal(name='timedOut')

    def __init__(self,device='ME', tag='TAG', environment=ENV, emitList=False):
        QThread.__init__(self)
        SkelCmdRec.__init__(self, device=device, tag=tag, environment=environment)
        self.setCallback(self.emitterL if emitList else self.emitter)
        self.setTimeOutCallback(self.ringAlarm)


    def ringAlarm(self):
        self.timedOut.emit()


    def emitter(self, cmd,val):
        self.respReceived.emit(val)


    def emitterL(self,cmd,val):
        if type(val) != list:
            val = [val]
        self.respReceivedL.emit([cmd]+val)