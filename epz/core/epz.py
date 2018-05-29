# EPZ 1.0
# Basic functions for general usage

import zmq
from .conf import Conf

ENV = {'context':zmq.Context.instance(),'epserver':'127.0.0.1','pubport':6661,'subport':6669}

def setEnvironment(filename = None):
  if filename is not None:
    c = Conf(filename)
    ENV['epserver'] = c['EPSERVER']
    ENV['pubport'] = c['PUBPORT']
    ENV['subport'] = c['SUBPORT']


class epzobject(object):

  def __init__(self, device='ME', tag='TAG', environment=ENV):
    self.context = environment['context']
    self.pubport = environment['pubport']
    self.subport = environment['subport']
    self.epserver = environment['epserver']
    self.device = device
    self.tag = tag
    self.setZMQ()

  def setZMQ(self):
    pass