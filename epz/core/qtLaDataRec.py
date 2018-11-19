# EPZ 1.0
# DATA receiver running in a separate Qt thread.
# Specialized Qt signals are emitted upon data reception; connect them to get them alive
# See skelDataRec.py for details
from .epz import ENV
from .skelLaDataRec import SkelLaDataRec

try:
    from PyQt5.QtCore import pyqtSignal, QThread
except:
    from PyQt4.QtCore import pyqtSignal, QThread


class QtLaDataRec(SkelLaDataRec, QThread):
    chunkReceived = pyqtSignal(list, name='chunkReceived')
    dataReceived = pyqtSignal(list, name='dataReceived')

    def __init__(self,device='ME', tag='TAG', environment=ENV):
        QThread.__init__(self)
        SkelLaDataRec.__init__(self, device=device, tag=tag, environment=environment)

    def _actOnData(self,v):

        self.dataReceived.emit(v)

    def _notification(self,v):
        self.chunkReceived.emit(v)