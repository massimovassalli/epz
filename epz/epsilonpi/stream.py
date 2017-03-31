from ..core.cmd import CMD
from ..core.cmdRec import CMDREC
from ..core.data import DATA
from ..core.dataRec import DataRec

import threading

class saver(threading.Thread):
    def __init__(self,filename, queue):
        threading.Thread.__init__(self)
        self.filename = filename
        self.queue = queue

    def run(self):
        f = open(self.filename)
        for r in self.queue.get():
            f.write('{}\t{}\t{}\t{}\n'.format(*r))
        f.close()


class client(object):
    def __init__(self,device,parameterName):
        self.device = device
        self.pName = parameterName
        self.valueChanged = None
        self.sender = CMD(device=device,tag=self.pName)
        self.sink = DataRec(device=device,tag=self.pName+'_STREAM')
        self.fnamecount = 0
        self.basename = './test'
        self.extension = '.txt'
        self.sink.notify = False
        self.autosave = False
        self.sink.setSaveCallback(self.save)

    def save(self,v):
        if v is False:
            if self.autosave is False:
                self.sink.flushing = True
            else:
                if len(self.sink._queue)>1:
                    self.fnamecount+=1
                    ss = saver(self.basename+':04'.format(self.fnamecount)+self.extension,self.sink._queue.pop(0))
                    ss.start()

    def setDataCallback(self,callback):
        self.sink.setDataCallback(callback)
        self.sink.notify = True

    def setValueCallback(self,callback):
        self.sink.setValueCallback(callback)

    def setOverloadCallback(self,callback):
        self.sink.setOverloadCallback(callback)

    def start(self,sync=True,fake=False):
        self.sink.start()
        if fake is True:
            self.setValueCallback(print)
            self.setOverloadCallback(lambda x: print('OVR: {}'.format(x)))

    def stop(self):
        self.sink.listen = False

    def pause(self):
        self.sender.send('PAUSE')

    def resume(self):
        self.sender.send('RESUME')


class server(object):
    def __init__(self,device,parameterName):
        self.device = device
        self.pName = parameterName
        self.sender = CMD(device=device,tag=self.pName)
        self.receiver = CMDREC(device=device,tag=self.pName)
        self.receiver.setCallback(self.setValue)
        self.producer = DATA(device=device,tag=self.pName+'_STREAM')
        self.type = float #for arrays use self.type = lambda x : [float(y) for y in x]
        self._value = None
        self.execute = lambda x : True

    def start(self,fake = False):
        self.receiver.start()
        if fake is True:
            self.execute = lambda x:  True if x<12 else False
            self._value = 0
        #fai partire il thread che fa l'acquisizione e mettici dentro self.produce

    #to be executed in another thread
    def produce(self):
        #implement the production loop
        self.producer.send(1,1,1)

    def stop(self):
        self.receiver.listen = False
        self.sender.send('EXIT')

    def setValue(self,cmd,val):
        if cmd == 'SET':
            newvalue = self.type(val)
            if newvalue==self._value:
                return
            if self.execute(newvalue) is True:
                self._value = newvalue
                self.sender.send('VAL',newvalue)
        elif cmd == 'GET':
            self.sender.send('VAL', self._value)
        elif cmd == 'EXIT':
            self.receiver.listen = False

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        newvalue = self.type(val)
        if newvalue != self._value:
            if self.execute(newvalue) is True:
                self._value = newvalue
                self.sender.send('VAL',newvalue)