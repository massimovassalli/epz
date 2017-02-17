# EPZ 1.0
# DATA receiver running in a separate Qt thread.
# Specialized Qt signals are emitted upon data reception; connect them to get them alive
# See skelDataRec.py for details
from .epz import ENV
from .skelDataRec import SkelDataRec

try:
    from PyQt5.QtCore import pyqtSignal, QThread
except:
    from PyQt4.QtCore import pyqtSignal, QThread


class QtDATA(SkelDataRec, QThread):
    chunkReceived = pyqtSignal(list, name='chunkReceived')
    xDataReceived = pyqtSignal(float, name='xDataReceived')
    yDataReceived = pyqtSignal(float, name='yDataReceived')
    zDataReceived = pyqtSignal(float, name='zDataReceived')
    stateChanged = pyqtSignal(bool, name='stateChanged')
    overloadChanged = pyqtSignal(bool, name='overloadChanged')

    def __init__(self,device='ME', tag='TAG', environment=ENV):
        QThread.__init__(self)
        SkelDataRec.__init__(self, device=device, tag=tag, environment=environment)

    def _actOnValue(self,data):
        self.xDataReceived.emit(data[0])
        self.yDataReceived.emit(data[1])
        self.zDataReceived.emit(data[2])

    def _switchState(self,state):
        self.stateChanged.emit(state)

    def _switchLoad(self,state):
        self.overloadChanged.emit(state)

    def _actondata(self,v):
        self.chunkReceived.emit(v)