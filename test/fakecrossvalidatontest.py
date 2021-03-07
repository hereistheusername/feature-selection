import unittest

from src.cross_validation import leave_one_out_cross_validation

class FakeCrossValidationTestCase(unittest.TestCase):
    def test_range(self):
        accuracy = leave_one_out_cross_validation(0,0,0)
        self.assertLessEqual(accuracy, 1)
        self.assertGreaterEqual(accuracy, 0)