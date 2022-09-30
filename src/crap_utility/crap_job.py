from crap_logger import crap_logger

def job():
    logger.info('What? 0.1')

def job2():
    print('What? (with print)')

def main():
    job()

logger = crap_logger()

if __name__ == "__main__":
    main()