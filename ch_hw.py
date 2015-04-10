import epz
epz.EPSERVER = '193.43.20.118'
import epdspic as pic

class DACvalue(epz.hardware):
    def __init__(self, hwname):
        super(DACvalue, self).__init__(hwname, 0.0)
        self.ser = pic.DACdev() #MN: DACdev initially resets to 0 the output value

    def update(self, v):
        """
        @type var:bool
        """
        self.ser.setValue(v)
        return True

class etvoila(epz.hardware):
    def acquire(self):
        data = pic.data()
        while self.goahead:
            v = data.read()
            self.myqueue.put(v)

if __name__ == '__main__':
    dev = epz.device('EP')
    dev.daemon = False
    dev.start()

#    dev.append(DACvalue('dac'))
    dev.append(etvoila('data',signal=True))
