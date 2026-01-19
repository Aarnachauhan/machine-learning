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

  first refresh the kernel (restart) otherwise error
  

import logging
#config the basic logging setting
logging.basicConfig(
    filename='app.log', #because of this , all the messages will b added in this file
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s -%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

#log messages
logging.debug("this is logging message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")
