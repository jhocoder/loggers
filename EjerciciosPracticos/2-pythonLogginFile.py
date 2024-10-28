import logging

logging.basicConfig(level=logging.ERROR, 
                    filename = "registro.log", filemode="a", format = "%(name)s - %(levelname)s - %(message)s")

logging.critical('Soy muy critico')
logging.debug('This will get logged to a file')
logging.warning("Soy un debuger man")
logging.info('Info info....')
logging.error('Esto es un error')
