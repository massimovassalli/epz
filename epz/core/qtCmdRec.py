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

  def __init__(self,device='ME', tag='TAG', environment=ENV):
    QThread.__init__(self)
    SkelCmdRec.__init__(self, device=device, tag=tag, environment=environment)

  def react(self, resp):
    self.respReceived.emit(resp)