#
# Copyright (C) 2016-2018 Ettore Landini
#
# v 1.0.33.1

## @package epzParam
# This module contains the implementation EpzParam, an object synchronized with the NanoUP raspberries used to store
# and modify the values of keys parameters used by both the firmware and the client software
#


from time import sleep
from datetime import datetime

from epz.core.cmd import CMD
from epz.core.cmdRec import CMDREC


#Generic constants
WAITFORPARAM = 0.1
COUNTSFORPARAMS = 50
GETRETRY = 5

#EPZ constants
SPISEND = 'SPISEND'
SPITX = 'SPITX'
CMDTAG = 'CMD'
DATATAG = 'DATA'
REQTAG = 'REQPAR'
RESPTAG = 'SNDPAR'


## class EpzParam
class EpzParam(object):

    ## Class constructor
    # @param device String: The name of the epz device to interrogate
    # @param paramname String: This string is used to create the set and get commands (SET_+paramname and GET_paramname)
    # @param parletter String: The letter used by the raspberry C written server program to identify the parameter
    # @param sendtag String: The epz object tag used to identify the PUB channel to set the parameter value
    # @param sendgettag String: The epz object tag used to identify the PUB channel to get the parameter value
    # @param gettag String: The epz object tag used to identify the SUB channel to get the parameter value
    # @param waitToAsk Float: A time interval to wait after each get instruction
    # @param waitToGet Float: A time interval while waiting for a get request response
    # @param waitCnt Integer: A counter used to monitor a get request success
    # @param getRetry Integer: The maximum number of times the parameter value is requested before raising a communication error
    # @param conversion Object: It can be a float or a callable object. It is used to convert the data to the format needed by the epz server
    # @param valuechanged Callable: A callable object called once self._value has changed
    # @param valuechanging Callable: A callable object called right before sending the new value to the server
    # @param readonly Boolean: If True the parameter is read only
    # @param reconvert Object: It can be a float or a callable object. It is used to reconvert the data from the format needed by the epz server
    # @param verbose Boolean: If True enables a series of print that describe the class behaviour
    # @param execlog Boolean: If True all the class member functions will print their name when called
    def __init__(self,device,paramname,parletter,sendtag=CMDTAG,sendgettag=REQTAG,gettag=RESPTAG,waitToAsk=0.1,
                 waitToGet=WAITFORPARAM,waitCnt=COUNTSFORPARAMS,getRetry=GETRETRY,conversion=1.0,
                 valuechanged=None,valuechanging=None,readonly=False,reconvert=None,verbose=False,execlog=False):

        if execlog:
            print('{1}.__init__ called at\t{0}'.format(datetime.now(), type(self).__name__))

        self.device = device
        self._valueChanged = valuechanged
        self._valueChanging = valuechanging
        self.pName = str(paramname)
        self.pLetter = str(parletter)
        self._conversion = conversion
        self._reconvert = reconvert
        self.getName = 'GET_'+self.pName
        self.setName = 'SET_' + self.pName
        self.sender = CMD(device=device,tag=sendtag)
        self.getter = CMD(device=device,tag=sendgettag)
        self.receiver = CMDREC(device=device,tag=gettag)
        self.receiver.setCallback(self.setValue)
        self.type = float #for arrays use self.type = lambda x : [float(y) for y in x]
        self._value = None
        self.waitToGet = waitToGet
        self.waitToAsk = waitToAsk
        self.waitCnt = waitCnt
        self.getRetry = getRetry
        #self.stillWaiting = False
        self.readOnly = readonly
        self._verbose = verbose
        self._execLog = execlog


    ## It starts the response receiver
    # @param sync Boolean: If True, self.syncValue and self.reSyncher will be called
    # @param fake Boolean: If True the valueChanged function will be set as "print"
    def start(self,sync=True,fake=False):
        if self._execLog:
            print('{1}.start called at\t{0}'.format(datetime.now(), type(self).__name__))
        self.receiver.start()
        if fake is True:
            self._valueChanged = print
        if sync is True:
            self.syncValue()
            self.reSyncher()


    ## Stops the receiver and call syncValue and reSyncher in order to properly stop the Thread
    def stop(self):
        if self._execLog:
            print('{1}.stop called at\t{0}'.format(datetime.now(), type(self).__name__))
        self.receiver.listen = False
        self.syncValue()
        self.reSyncher()


    ## Is the function called when the response from the server is received:
    # @param cmd String: The letter of the parameter currently returned on the SNDPAR channel. If it's not equal to self.pLetter, the value is ignored
    # @param val String: The value returned by the server
    def setValue(self,cmd,val):
        if self._execLog:
            print('{1}.setValue called at\t{0}'.format(datetime.now(), type(self).__name__))
        if self._verbose:
            print('Letter should be \'{0}\' and is \'{1}\''.format(self.pLetter,cmd))
            print('Value: {0}'.format(val))
            #print('Still waiting? {0}'.format(self.stillWaiting))

        if cmd != self.pLetter:
            if self._verbose:
                print('Letter should be \'{0}\' and is \'{1}\''.format(self.pLetter, cmd))
            return
        #if not self.stillWaiting:
        #    return
        #self.stillWaiting = False
        if self._reconvert is None:
            if not callable(self._conversion):
                newvalue = self.type(val)/self._conversion
        else:
            if callable(self._reconvert):
                newvalue = self._reconvert(self.type(val))
            else:
                newvalue = self.type(val)*self._reconvert

        self._value = newvalue

        if self._verbose:
            print('self._value: {0}'.format(self._value))


    ## Repeat the syncValue function untill a response is received or untill the maximum number of trials has been reached
    def reSyncher(self):
        if self._execLog:
            print('{1}.reSyncher called at\t{0}'.format(datetime.now(), type(self).__name__))
        j = 0
        for j in range(self.getRetry):
            cnt = 0
            while cnt < self.waitCnt and self._value is None:  # and self.stillWaiting:
                sleep(self.waitToGet)
                cnt += 1
            if cnt < self.waitCnt:
                break
            self.syncValue()
        if j == self.getRetry - 1:
            raise Exception('Communication error')


    ## Query the server for the currently stored parameter's value
    def syncValue(self):
        if self._execLog:
            print('{1}.syncValue called at\t{0}'.format(datetime.now(), type(self).__name__))
        #self.stillWaiting = True
        if self._verbose:
            print("syncValue - Sent: {0}".format(self.getName))
        self.getter.send(self.getName)


    ## Getter for the self.value property
    @property
    def value(self):
        if self._execLog:
            print('{1}.value called at\t{0}'.format(datetime.now(), type(self).__name__))
        return self._value


    ## Setter for the self..value property
    # @param value Float: The new value to set
    @value.setter
    def value(self, val):
        if self._execLog:
            print('{1}.value called at\t{0}'.format(datetime.now(), type(self).__name__))
        if self.readOnly:
            return
        if callable(self._conversion):
            newvalue = self._conversion(self.type(val))
        else:
            newvalue = self.type(val)*self._conversion
        if self._valueChanging is not None:
            returned = self._valueChanging()
            if returned is not None and type(returned) == bool:
                if returned:
                    return
        self._value = None
        i = 0
        for i in range(self.getRetry):
            self.sender.send(self.setName,newvalue)
            sleep(self.waitToAsk)
            self.syncValue()
            # TODO: find a way to check the returned value
            if self._value is not None:
                if self._valueChanged is not None:
                    self._valueChanged(self._value)
                break
            self.reSyncher()
        if i == self.getRetry - 1:
            raise Exception('Comunication error')


    ## The self.conversion property getter
    @property
    def conversion(self):
        if self._execLog:
            print('{1}.conversion called at\t{0}'.format(datetime.now(), type(self).__name__))
        return self._conversion


    ## The self.conversion property setter
    # @param v Object: It can be a Float or a callable object
    #
    # The self._value value is reconverted in order to represent the remotely stored value
    @conversion.setter
    def conversion(self,v):
        if self._execLog:
            print('{1}.conversion called at\t{0}'.format(datetime.now(), type(self).__name__))
        if v == self._conversion:
            return

        if callable(v):
            pass
            #remoteVal = self._conversion(self.value)
            #self._value = self._reconvert(remoteVal)
        else:
            remoteVal = self.value*self._conversion
            self._value = remoteVal/v

        self._conversion = v


    ## The self.reconvert property getter
    @property
    def reconvert(self):
        if self._execLog:
            print('{1}.reconvert called at\t{0}'.format(datetime.now(), type(self).__name__))
        return self._reconvert

    ## The self.reconvert property setter
    # @param v Object: It can be a Float or a callable object
    @reconvert.setter
    def reconvert(self, v):
        if self._execLog:
            print('{1}.reconvert called at\t{0}'.format(datetime.now(), type(self).__name__))
        if v == self._reconvert:
            return

        if callable(v):
            remoteVal = self._conversion(self.value)
            self._value = v(remoteVal)
        else:
            return

        self._reconvert = v


    ## Sets the valueChanged function
    # @param func Callable: A callable object
    def setValueChanged(self,func):
        if self._execLog:
            print('{1}.setValueChanged called at\t{0}'.format(datetime.now(), type(self).__name__))
        if not callable(func):
            raise Exception('You must specify a callable object')
        self._valueChanged = func


    ## Sets the valueChanging function
    # @param func Callable: A callable object
    def setValueChanging(self, func):
        if self._execLog:
            print('{1}.setValueChanging called at\t{0}'.format(datetime.now(), type(self).__name__))
        if not callable(func):
            raise Exception('You must specify a callable object')
        self._valueChanging = func