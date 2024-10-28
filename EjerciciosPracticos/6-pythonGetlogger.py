import logging


logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()

file_handler = logging.FileHandler('app.log', mode ='a', encoding='utf-8')

logger.addHandler(console_handler)
logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('WARNING message')