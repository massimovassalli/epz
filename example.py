"""
EpsilonPi Device
"""

import zmq
import threading
import time

import configparser
config = configparser.ConfigParser()
config.read('epz.ini')

EPSERVER = config['ZMQ']['EPSERVER']
SUBPORT = config['ZMQ']['SUBPORT']
PUBPORT = config['ZMQ']['PUBPORT']
SERPORT = config['PIC']['SERPORT']
SPIPORT = config['PIC']['SPIPORT']
ISFW = config.getboolean('ZMQ','FORWARDING')

CONTEXT = zmq.Context.instance()

subsocket = CONTEXT.socket(zmq.SUB)
subsocket.setsockopt_string(zmq.SUBSCRIBE,"TEST:STATE:")
subsocket.connect("tcp://{0}:{1}".format(EPSERVER,SUBPORT))

#psocket = CONTEXT.socket(zmq.PAIR)
#psocket.connect("tcp://{0}:{1}".format(EPSERVER,SPIPORT))

while True:
    body= subsocket.recv_string()
    print(body)