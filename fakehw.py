"""
EpsilonPi Fake Hardware for tests
"""

import epz
import time
import zmq
import threading

loop = True
wait = 0.001

ENV = epz.Environment('test.conf')
DEVICE = ENV.device
TIMEBASE = 20

def receive():
    global loop
    global wait
    socket = ENV.context.socket(zmq.SUB)
    head = "{0}:CMD:".format(DEVICE)
    socket.setsockopt_string(zmq.SUBSCRIBE,head)
    socket.connect("tcp://{0}:{1}".format(ENV.epserver,ENV.subport))
    while loop:
        #  Wait for next request from client
        message = socket.recv_string()
        cmd = message.strip(head)
        if cmd[0] == 'K':
            print('FakeSerial: KILL signal received ...')
            time.sleep (1)
            loop = False
        else:
            pieces = cmd.split(':')
            letter,pars = pieces[0],pieces[1:]
            print ("Received letter: {0} with parameters {1}".format(letter,pars))
            if letter == '8':
                newtime = int(pars[0])/1000000.0
                print('Changed production interval to {0}us'.format(newtime*1000000.0))
                wait = newtime

        time.sleep (1)


def send():
    import numpy as np
    global loop
    global wait
    ssock = ENV.context.socket(zmq.PUB)
    ssock.connect("tcp://{0}:{1}".format(ENV.epserver,ENV.pubport))
    inittime = time.perf_counter()
    i = 0
    j = 0
    while loop:
        i += 1
        j += 1
        n = np.random.random() / 10.0
        omega = 27.0
        st = np.sin(2*np.pi*float(i)*omega/10000.0)+n
        ct = np.cos(2*np.pi*float(i)*omega/10000.0)-n
        tmp = int(1000000.0*(time.perf_counter()-inittime)/TIMEBASE)
        msg = '{0}:DATA:{1}:{2}:{3}'.format(DEVICE,tmp,st,ct)
        ssock.send_string(msg)
        time.sleep(wait)

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
