import unittest

from src.datareader import read_data
from src.featuresearch import feature_search_demo

class FeatureSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(sel):
        sel.data_path = 'data/fivelines.txt'

    def test_demo_output(self):
        data = read_data(self.data_path)
        feature_search_demo(data)


if __name__ == '__main__':
    unittest.main()