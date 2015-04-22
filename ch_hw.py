import epz3 as epz
epz.EPSERVER = '193.43.20.118'
import epdspic as pic

class DACvalue(epz.HWparameter):

    def init(self):
        self.ser = pic.DACdev() #MN: DACdev initially resets to 0 the output value

    def update(self,v):
        try:
            self.ser.setValue(v)
        except:
            return False
        return True

class ADCread(epz.HWsignal):

    def init(self):
        self.pic = pic.data()

    def acquire(self):
        return self.pic.read()

if __name__ == '__main__':
    dev = epz.Device('EP')
    dev.daemon = False
    dev.start()

    dev.append(DACvalue('dac'))
    dev.append(ADCread('data'))
