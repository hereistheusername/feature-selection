import unittest

from src.datareader import read_data

class DataReaderTestCase(unittest.TestCase):
    def test_validation(self):
        small_data_path = 'data/CS170_SMALLtestdata__15.txt'
        large_data_path = 'data/CS170_largetestdata__55.txt'
        small_data = read_data(small_data_path)
        (n,m) = small_data.shape
        self.assertEqual(n, 300)
        self.assertEqual(m, 11)

        large_data = read_data(large_data_path)
        (n,m) = large_data.shape
        self.assertEqual(n, 500)
        self.assertEqual(m, 101)

