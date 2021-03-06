import unittest

from src.datareader import read_data
from src.featuresearch import forward_feature_search

class FeatureSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(sel):
        sel.data_path = 'data/fivelines.txt'
        sel.small_data_path = 'data/CS170_SMALLtestdata__15.txt'
        sel.large_data_path = 'data/CS170_largetestdata__55.txt'

    def test_demo_output(self):
        data = read_data(self.small_data_path)
        forward_feature_search(data)


if __name__ == '__main__':
    unittest.main()