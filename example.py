from crap_utility.crap_logger import crap_logger
from crap_utility.crap_job import job1, job2

logger = crap_logger()

if __name__ == "__main__":
    logger.info('Main of: %s', __name__)
    job1()
    job2()