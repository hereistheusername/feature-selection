import unittest

from src.cross_validation import leave_one_out_cross_validation
from src.datareader import read_data

class SpecialValidationTestCase(unittest.TestCase):
    
    def test_dataset_95(self):
        data = read_data('data/CS170_small_special_testdata__95.txt')
        (n,m) = data.shape
        accuracy = leave_one_out_cross_validation(data, {7,4,6},0)
        self.assertAlmostEqual(round(accuracy,2), 0.92)
        all_features = set([n for n in range(1,m)])
        accuracy = leave_one_out_cross_validation(data, all_features,0)
        self.assertAlmostEqual(round(accuracy,2), 0.69)

    def test_dataset_96(self):
        data = read_data('data/CS170_small_special_testdata__96.txt')
        (n,m) = data.shape
        accuracy = leave_one_out_cross_validation(data, {2,3,9},0)
        self.assertAlmostEqual(round(accuracy,2), 0.94)
        all_features = set([n for n in range(1,m)])
        accuracy = leave_one_out_cross_validation(data, all_features,0)
        self.assertAlmostEqual(round(accuracy,2), 0.71)

    def test_dataset_97(self):
        data = read_data('data/CS170_small_special_testdata__97.txt')
        (n,m) = data.shape
        accuracy = leave_one_out_cross_validation(data, {2,9,7},0)
        self.assertAlmostEqual(round(accuracy,2), 0.9)
        all_features = set([n for n in range(1,m)])
        accuracy = leave_one_out_cross_validation(data, all_features,0)
        self.assertAlmostEqual(round(accuracy,2), 0.69)

    def test_dataset_98(self):
        data = read_data('data/CS170_small_special_testdata__98.txt')
        (n,m) = data.shape
        accuracy = leave_one_out_cross_validation(data, {7,9,8},0)
        self.assertAlmostEqual(round(accuracy,2), 0.92)
        all_features = set([n for n in range(1,m)])
        accuracy = leave_one_out_cross_validation(data, all_features,0)
        self.assertAlmostEqual(round(accuracy,2), 0.77)

    def test_dataset_99(self):
        data = read_data('data/CS170_small_special_testdata__99.txt')
        (n,m) = data.shape
        accuracy = leave_one_out_cross_validation(data, {6,1,5},0)
        self.assertAlmostEqual(round(accuracy,2), 0.91)
        all_features = set([n for n in range(1,m)])
        accuracy = leave_one_out_cross_validation(data, all_features,0)
        self.assertAlmostEqual(round(accuracy,2), 0.72)