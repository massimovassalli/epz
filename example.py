"""
EpsilonPi Device
"""

import epz
import numpy as np

loop = True
log = False

import sys
fconf = 'test.conf'
if len(sys.argv) == 2:
    fconf = sys.argv[1]
ENV = epz.Environment(fconf)

TIMEBASE = 20.0 #in us
TIMETIME = 50.0

class myDat (epz.DATA):

    def actondata(self,v):
        t = np.array(v[0])
        dt = t[1:]-t[0:-1]

        mini = np.min(dt)
        maxi = np.max(dt)

        tottime = (t[-1]-t[0])*TIMEBASE
        freq = self.chunk*1000.0/tottime

        print('MIN [{0} of {1}us] - MAX [{0} of {1}us] - FREQ [kHz]'.format(TIMETIME,TIMEBASE))
        print ('{0} - {2} - {4}'.format(int(mini/TIMETIME),mini*TIMEBASE,int(maxi/TIMETIME),maxi*TIMEBASE,freq))

dat = myDat(ENV)
dat.ttime = 0
dat.chunk = 1000
cmd = epz.CMD(ENV)

dat.start()
dat.notify = True

while loop:
    message = input("Give me the command:parameter string to be sent to the TEST device:")
    if message == 'K':
        loop = False
        dat.goahead = False
        cmd.send('K')
    elif message == 'switch':
        dat.notify = not dat.notify
        print('--------------')
    else:
        letter,pars = message.split(':')
        if letter == '8':
            TIMETIME = int(pars)/TIMEBASE
        cmd.send(letter, pars)