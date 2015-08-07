"""
EpsilonPi Fake Hardware for tests
"""

import epz
import time
import zmq
import threading

loop = True
inittime = time.time()

ENV = epz.Environment('epz.conf')
DEVICE = ENV.device


def receive():
    global loop
    socket = ENV.context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE,"{0}:CMD:".format(DEVICE))
    socket.connect("tcp://{0}:{1}".format(ENV.epserver,ENV.epserver))
    while loop:
        #  Wait for next request from client
        message = socket.recv_string()
        cmd = message.strip('{0}:CMD:'.format(DEVICE))
        if cmd[0] == 'K':
            print('FakeSerial: KILL signal received ...')
            time.sleep (1)
            loop = False
        else:
            print ("Received request: {0}".format(message))
        time.sleep (1)


def send():
    import numpy as np
    global loop
    ssock = ENV.context.socket(zmq.PUB)
    ssock.connect("tcp://{0}:{1}".format(ENV.epserver,ENV.pubport))

    i = 0
    j = 0
    while loop:
        i += 1
        j += 1
        n = np.random.random() / 10.0
        omega = 27.0
        st = np.sin(2*np.pi*float(i)*omega/10000.0)+n
        ct = np.cos(2*np.pi*float(i)*omega/10000.0)-n
        tmp = int(1000000.0*(time.time()-inittime)/20.0)
        msg = '{0}:DATA:{1}:{2}:{3}'.format(DEVICE,tmp,st,ct)
        ssock.send_string(msg)
        time.sleep(0.001)

import forwarder as fw
#f = fw.Forwarder()
#f.start()

acpol = threading.Thread(target=receive)
acpol.daemon = False
acpol.start()

ac2 = threading.Thread(target=send)
ac2.daemon = False
ac2.start()

print('I\'m now producing ...')
