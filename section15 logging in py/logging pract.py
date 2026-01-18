python logging ->

-------------------------------------------

import logging
#config the basic logging setting
logging.basicConfig(level=logging.DEBUG)

#log messages with diff severity level message
logging.debug("this is logging message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")
  
o/p
DEBUG:root:this is logging message
INFO:root:this is info message
WARNING:root:this is warning message
ERROR:root:this is error message
CRITICAL:root:this is critical message

---------------------------------------------------------

  
  
