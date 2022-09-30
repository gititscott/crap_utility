import logging

def crap_logger(name='crap'):
    logger = logging.getLogger(name)
    logging.basicConfig(
        format='%(asctime)s - %(levelname)-5s - %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logger
