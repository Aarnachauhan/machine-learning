this is about creating multiple loggers for differnet part of the app
import logging 
logger1=logging.getLogger('module1')
logger1.setLevel(logging.DEBUG)

#create logger for module 2
logger2=logging.getLogger('module 2')
logger2.setLevel(logging.WARNING)

logging.basicConfig(
    
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s -%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

logger1.debug("this is debug message")
logger2.warning("this is warning message")
logger1.error("this is error message")

o/p
2026-01-19 07:47:02-module1 -DEBUG-this is debug message
2026-01-19 07:47:02-module 2 -WARNING-this is warning message
2026-01-19 07:47:02-module1 -ERROR-this is error message

phele module1, module 2 ki jagah roots likha hota tha
