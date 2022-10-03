import pandas as pd
import numpy as np
from crap_utility.crap_logger import crap_logger

def crap_frame():
    logger.info('Creating dataframe...')
    return pd.Series([1, 3, 5, np.nan, 6, 8])

def main():
    df = crap_frame()

logger = crap_logger()

if __name__ == "__main__":
    logger.info('Main of: %s', __name__)
    main()
