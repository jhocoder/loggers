import os
import logging

class Logger():
   
    def _set_logger(self):
        log_directory = 'logs/'
        log_filename = 'app_buena.log'

        logger = logging.getLogger(__name__)
        logger.setLevel('DEBUG')

        log_path = os.path.join(log_directory, log_filename)
        file_handler = logging.FileHandler(log_path, encoding='utf-8',
                                           mode='a')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('{asctime} | {levelname} | {message}')


