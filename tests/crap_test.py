from crap_utility.crap_logger import crap_logger
from crap_utility.crap_job import job1, job2
from crap_utility.crap_pandas import crap_frame
import pandas as pd

import unittest

class TestStringMethods(unittest.TestCase):

    def test_job1(self):
        logger.info('This is: %s', __name__)
        self.assertEqual(job1(), None)
    
    def test_job2(self):
        logger.info('This is: %s', __name__)
        self.assertEqual(job2(), None)

    def test_crap_frame(self):
        logger.info('Testing data frame creation')
        self.assertEqual(type(crap_frame()), pd.Series)

logger = crap_logger()

if __name__ == "__main__":
    logger.info('Main of: %s', __name__)
    unittest.main()
