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
    self.context = ENV['context']
    self.pubport = ENV['pubport']
    self.subport = ENV['subport']
    self.epserver = ENV['epserver']
    self.device = device
    self.tag = tag
    print('epz: {0}'.format(ENV))
    self.setZMQ()

  def setZMQ(self):
    pass