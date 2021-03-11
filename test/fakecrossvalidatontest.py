import unittest

from src.cross_validation import leave_one_out_cross_validation
from src.datareader import read_data

class FakeCrossValidationTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(sel):
        sel.data_path = 'data/CS170_small_special_testdata__95.txt'

    def test_range(self):
        data = read_data(self.data_path)
        accuracy = leave_one_out_cross_validation(data,{7,4},6)
        self.assertLessEqual(accuracy, 1)
        self.assertEqual(accuracy, 0.92)
        self.assertGreaterEqual(accuracy, 0)