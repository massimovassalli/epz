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






#psocket = CONTEXT.socket(zmq.PAIR)
#psocket.connect("tcp://{0}:{1}".format(EPSERVER,SPIPORT))

loop = True
log = False
def receive():
    global loop
    global log
    subsocket = CONTEXT.socket(zmq.SUB)
    subsocket.setsockopt_string(zmq.SUBSCRIBE,"TEST:STATE:")
    subsocket.connect("tcp://{0}:{1}".format(EPSERVER,SUBPORT))
    while loop:
        body= subsocket.recv_string()
        if log:
            print('I received an update about: {0}'.format(body))

acpol = threading.Thread(target=receive)
acpol.daemon = True
acpol.start()

ssock = CONTEXT.socket(zmq.PUB)
ssock.connect("tcp://127.0.0.1:{0}".format(PUBPORT))

while loop:
    message = input("Give me the command:parameter string to be sent to the TEST device:")
    if message == 'KILL':
        loop = False
    if message == 'LOG':
        if log:
            log=False
        else:
            log=True
    msg = '{0}:{1}:{2}'.format('TEST','ACTION',message)
    ssock.send_string(msg)
