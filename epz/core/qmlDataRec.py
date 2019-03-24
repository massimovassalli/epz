# EPZ 2.1
# DATA receiver running in a separate Qt thread.
# Specialized Qt signals are emitted upon data reception; connect them to get them alive
# See skelDataRec.py for details
from .epz import ENV
from .skelDataRec import SkelDataRec

from PySide2.QtCore import QThread, Signal, Slot


class QMLDATA(SkelDataRec, QThread):
    chunkReceived = Signal(list, name='chunkReceived')
    xDataReceived = Signal(float, name='xDataReceived')
    yDataReceived = Signal(float, name='yDataReceived')
    zDataReceived = Signal(float, name='zDataReceived')
    stateChanged = Signal(bool, name='stateChanged')
    overloadChanged = Signal(bool, name='overloadChanged')

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