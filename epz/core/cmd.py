# EPZ 1.0
# CMD object to broadcast commands for a specific device
# one COMMAND can be associated to a list of VALUES

import zmq
from .epz import epzobject

class CMD(epzobject):
  def setZMQ(self):
    self._socket = self.context.socket(zmq.PUB)
    self._socket.connect("tcp://{0}:{1}".format(self.epserver, self.pubport))

  def send(self, cmd='', values=[]):
    msg = '{0}:{1}:{2}'.format(self.device, self.tag,cmd)
    if type(values) != list :
        values = [values]
    for v in values:
        msg = msg + ':' + str(v)
    self._socket.send_string(msg)