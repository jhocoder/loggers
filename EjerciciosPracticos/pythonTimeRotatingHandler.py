import  logging, time

from logging.handlers  import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

handler = TimedRotatingFileHandler('logs/time_app.log', when='M', interval=1)

logger.addHandler(handler)

while True:
    time.sleep(1)
    logger.info('Algo simple {}'.format(time.time()))
