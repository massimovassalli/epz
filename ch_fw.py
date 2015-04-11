#import epz library
import epz3 as epz
#instantiate the forwarder and start 
fw = epz.Forwarder()
#note: fw.daemon is internally set to False, to avoid closure of the 
#forwarding thread just at the end of the script.
fw.start()