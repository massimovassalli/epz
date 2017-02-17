# EPZ 1.0
# CMD receiver running in a separate python thread.
# See cmdDataRec.py for details

import threading
from .skelCmdRec import SkelCmdRec
from .epz import ENV

class CMDREC(SkelCmdRec, threading.Thread):
  def __init__(self, device='ME', tag='TAG', environment=ENV):
    threading.Thread.__init__(self)
    SkelCmdRec.__init__(self, device=device, tag=tag, environment=environment)
