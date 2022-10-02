from crap_utility.crap_logger import crap_logger

def job1():
    logger.info('What? 0.1')

def job2():
    print('What? (with print)')

def main():
    job1()
    job2()

logger = crap_logger()

if __name__ == "__main__":
    logger.info('Main of: %s', __name__)
    main()
