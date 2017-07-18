# EPZ 1.0
# CMD receiver running in a separate Qt thread.
# Specialized Qt signals are emitted upon data reception; connect them to get them alive
# See skelCmdRec.py for details

from .skelCmdRec import SkelCmdRec
from .epz import ENV

try:
  from PyQt5.QtCore import pyqtSignal, QThread
except:
  from PyQt4.QtCore import pyqtSignal, QThread


class QtCMDREC(SkelCmdRec, QThread):

    respReceived = pyqtSignal(str, name='respReceived')
    respReceivedL = pyqtSignal(list,name='respReceivedL')
    timedOut = pyqtSignal(name='timedOut')

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
        self.respReceivedL.emit([cmd,val])