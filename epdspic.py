"""
EP-dspic
Main library to communicate with RaspdsPIC board
"""
from libbcm2835._bcm2835 import *
import serial
import binascii

ADRANGE = 1.0
BITSTEP = ADRANGE/65536.0

DACVREF = 5.0
DACUNIPOLAR = 0
DACBIPOLAR = 1
DACPOLAR = DACUNIPOLAR

def convto16bit(vbin):
    """
    Convert 16bit data into voltage accounting for acquisition range
    """
    if (vbin > 0x8000):
        v=-(BITSTEP*vbin-ADRANGE)
    else:
        v=-(BITSTEP*vbin)
    return v
        
        
class data:
    def __init__(self):
        """
        Class for managing SPI transfer with dsPIC
        initialization done with custom values
        """
        self.open=False
        #opening the SPI communication
        if not bcm2835_init():
            return
        self.open=True
        #configuring SPI channel with Marco's flavour
        bcm2835_spi_begin()
        bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST)      # The default
        bcm2835_spi_setDataMode(BCM2835_SPI_MODE1)                   # NOT The default
        bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_32)    # NOT The default
        bcm2835_spi_chipSelect(BCM2835_SPI_CS0)                      # The default
        bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW)      # The default

    def close(self):
        self.open = False
        bcm2835_spi_end()
        bcm2835_close()

    def transfer(self,data):
        """
        Transfer 8bit data to/from dsPIC through SPI.
        NB: The dsPIC side should be configured to write 8bit data
        """
        databack = bcm2835_spi_transfer(data)
        return databack

    def transfer16(self):
        """
        Transfer 16bit data to/from dsPIC through SPI.
        Data are obtained as string of chars and converted to 16bit int
        The dsPIC side should be configured to write 16bit data (NB: 16 != 2x8)
        """

        rbuf=b'00'
        bcm2835_spi_transfernb(b'0',rbuf,2)
        return int(binascii.hexlify(rbuf),16) # ^ 0x8000

    def read(self):
        vbin = self.transfer16()
        v = convto16bit(vbin)
        return v

class command(object):
    def __init__(self):
        ser = serial.Serial()
        ser.port = "/dev/ttyAMA0"
        ser.baudrate = 115200
        ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        ser.parity = serial.PARITY_NONE #set parity check: no parity
        ser.stopbits = serial.STOPBITS_ONE #number of stop bits
    
        #ser.timeout = None      #block read    
        ser.timeout = 1          #non-block read    
        #ser.timeout = 2         #timeout block read    
        ser.xonxoff = False      #disable software flow control    
        ser.rtscts = False       #disable hardware (RTS/CTS) flow control    
        ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control    
        ser.writeTimeout = 3     #timeout for write

        self.ser = ser

        self.cmdchar = 'D'

    def vtoAD5871(self,v):
        """
        Convert expected output in VOLT to the correct word for AD5871
        """
        n16bit = int(round(  (2**18 -1) * (v + DACVREF*self.polarity) / (DACVREF * (1+self.polarity)) ))
        nFull = (n16bit<<2)+0x100000
        nA = (nFull & 0xFF0000) >> 16
        nB = (nFull - (nA << 16) ) >> 8
        nC = nFull - (nA << 16) - (nB << 8)

        return nA,nB,nC

    def write(self,cmd):
        self.ser.open()
        self.ser.flushInput()   #flush input buffer, discarding all its contents
        self.ser.flushOutput()  #flush output buffer, aborting current output 
                                #and discard all that is in buffer
        #write data    
        self.ser.write(cmd.encode())
        self.ser.close()

    def setValue(self,v):
        self.write(self.cmdchar)
        coms = self.vtoAD5871(v)
        for com in coms:
            self.write(chr(com))


class ADCdev(data):
    pass


class DACdev(command):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.polarity = DACBIPOLAR
        self.setPolarity(self.polarity) #Set polarity also sets the value of the DAC to 0V
        self.value=0.0

    def setToZero(self):
        self.write('Z')

    def setPolarity(self,p=DACBIPOLAR):
        self.polarity = p
        self.write('P')
        pols = {DACUNIPOLAR:chr(0),DACBIPOLAR:chr(1)}
        self.write(pols[p])

    def sendChar(self,ch):
        self.write(ch)
