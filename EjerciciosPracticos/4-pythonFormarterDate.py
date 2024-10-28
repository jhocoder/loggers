import logging

# Configuración básica de logging
logging.basicConfig(
    format='%(asctime)s - %(message)s',
    datefmt='%d - %m - %y %H:%M:%S',
    style=' { '
    level=logging.DEBUG)

# Registro de información
logging.info("Admin logged in system")
