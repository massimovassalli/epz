
from ..core.cmd import CMD
from ..core.cmdRec import CMDREC
#REMOVE IT#################################
from epz.core.epz import ENV
print(ENV)
###########################################
class client(object):
    def __init__(self,device,parameterName):
        self.device = device
        self.pName = parameterName
        self.valueChanged = None
        self.sender = CMD(device=device,tag=self.pName)
        self.receiver = CMDREC(device=device,tag=self.pName)
        self.receiver.setCallback(self.setValue)
        self.type = float #for arrays use self.type = lambda x : [float(y) for y in x]
        self._value = None

    def start(self,sync=True,fake=False):
        self.receiver.start()
        if fake is True:
            self.valueChanged = print
        if sync is True:
            self.syncValue()

    def stop(self):
        self.receiver.listen = False

    def setValue(self,cmd,val):
        if cmd == 'VAL':
            newvalue = self.type(val)
            if newvalue==self._value:
                return
            self._value = newvalue
            if self.valueChanged is not None:
                self.valueChanged(newvalue)
        elif cmd == 'EXIT':
            self.receiver.listen = False
            self.sender.send('EXIT')

    def syncValue(self):
        self.sender.send('GET')

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        newvalue = self.type(val)
        if newvalue != self._value:
            self.sender.send('SET',newvalue)

class server(object):
    def __init__(self,device,parameterName):
        self.device = device
        self.pName = parameterName
        self.sender = CMD(device=device,tag=self.pName)
        self.receiver = CMDREC(device=device,tag=self.pName)
        self.receiver.setCallback(self.setValue)
        self.type = float #for arrays use self.type = lambda x : [float(y) for y in x]
        self._value = None
        self.execute = lambda x : True

    def start(self,fake = False):
        self.receiver.start()
        if fake is True:
            self.execute = lambda x:  True if x<12 else False
            self._value = 0

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