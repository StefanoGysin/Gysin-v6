# src/utils/logger.py
from loguru import logger

def setup_logger():
    logger.add("logs/gysin_ia.log", rotation="1 day")
    return logger