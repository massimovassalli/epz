# EPZ 1.0
# CMD receiver running in a separate python thread.
# See cmdDataRec.py for details

from threading import Thread
from .skelCmdRec import SkelCmdRec
from .epz import ENV

class CMDREC(SkelCmdRec, Thread):
  def __init__(self, device='ME', tag='TAG', environment=ENV):
    Thread.__init__(self)
    SkelCmdRec.__init__(self, device=device, tag=tag, environment=environment)
