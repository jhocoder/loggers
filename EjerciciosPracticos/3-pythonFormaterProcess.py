import logging

a = "El gato volador"

logging.basicConfig(format='%(process)d - %(levelname)s: %(message)s - %s')


logging.warning('This is a WARNING {}'.format(a))
logging.error('This is a Error  {}'.format(a))
#ver en administracion tarea
# while True:
#     pass
