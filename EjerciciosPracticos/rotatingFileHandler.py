import logging
from logging.handlers import RotatingFileHandler
import time

#cuando se llena archivo crea otro. maneja los archivos

#filename - Required
#mode - 'a' defect
#maxBytes - tamaño maximo antes de que ocurra la rotacion
#encoding - Encoding, system default
#delay -Used to delay cration until a write occurs
#backupCount - How many kig a files to keep


handler = RotatingFileHandler(filename='logs/log.out', maxBytes = 2058, backupCount=5)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel('DEBUG')

for _ in range(20):
    st = "The time is now {}".format(time.time())
    logger.debug(st)

    ### from time import gmtime, strftime 
    
    # strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

    