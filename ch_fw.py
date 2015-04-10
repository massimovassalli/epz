#import epz library
import epz
#instantiate the forwarder and start 
fw = epz.forwarder()
#note: fw.daemon is internally set to False, to avoid closure of the 
#forwarding thread just at the end of the script.
fw.start()