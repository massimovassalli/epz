# EPZ 2.1
# DATA receiver running in a separate Qt thread.
# Specialized Qt signals are emitted upon data reception; connect them to get them alive
# See skelLaDataRec.py for details
from .epz import ENV
from .skelLaDataRec import SkelLaDataRec

from PySide2.QtCore import QThread, Signal, Slot


class QMLLaDataRec(SkelLaDataRec, QThread):
    chunkReceived = Signal(list, name='chunkReceived')
    dataReceived = Signal(list, name='dataReceived')

    def __init__(self,device='ME', tag='TAG', environment=ENV):
        QThread.__init__(self)
        SkelLaDataRec.__init__(self, device=device, tag=tag, environment=environment)

    def _actOnData(self,v):

        self.dataReceived.emit(v)

    def _notification(self,v):
        self.chunkReceived.emit(v)