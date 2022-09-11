import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('log_monitro_salud.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
