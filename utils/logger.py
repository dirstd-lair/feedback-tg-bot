import logging
from logging.handlers import RotatingFileHandler

def get_logger(name):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = RotatingFileHandler("logs/logs.log", maxBytes=10**6, backupCount=5)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
