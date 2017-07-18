# EPZ 1.0
# Skeleton to create a CMD receiver object (counterpart of the CMD object)
# The class is designed to extend a threading class in standard python3 or a QtThread in Qt
# use the corresponding implementations, not this skeleton.

import zmq
from .epz import epzobject
from .cmd import CMD

class SkelCmdRec(epzobject):

  def setZMQ(self):
    self._callback = None
    self._timeOutCallback = None
    self._head = "{0}:{1}:".format(self.device, self.tag)  #This is the name of the subscribed thread on the EPSERVER
    self._socket = self.context.socket(zmq.SUB)
    self._socket.setsockopt_string(zmq.SUBSCRIBE, self._head)
    self._socket.connect("tcp://{0}:{1}".format(self.epserver, self.subport))
    self._stopit = CMD(device=self.device, tag=self.tag)

  def setTimeout(self,timeOut=0):

    if timeOut > 0:
      self.timeOut = timeOut
      self._socket.RCVTIMEO = timeOut

  def setCallback(self,callback):
    self._callback = callback

  def setTimeOutCallback(self,callback):
    self._timeOutCallback = callback

  def react(self, resp): #Action to be done when resp is received. This is implementation dependant
    if self._callback is not None:
      fragments = resp.split(':')
      cmd = fragments[0]
      val = None
      if len(fragments)>2:
        val = fragments[1:]
      elif len(fragments)==2:
        val = fragments[1]
      self._callback(cmd,val)

  def stop(self):
    self.listen = False
    self._stopit.send('stop')

  def run(self,oneShot = False):

    if oneShot:
      body = self._socket.recv_string()
      resp = body[len(self._head):].split(':')[0]
      return resp
    else:
      self.listen = True

    while self.listen:
      try:
        body = self._socket.recv_string()
      except:
        self.setZMQ()
        try:
          if self.timeOut > 0:
            print('timedOut epz')
            self._timeOutCallback()
            self.setTimeout(self.timeOut)
        except:
          pass
        continue
        #body = self._socket.recv_string()
      resp = body[len(self._head):]
      self.react(resp)