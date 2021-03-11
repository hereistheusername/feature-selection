import unittest
from test import fakecrossvalidatontest
from test import datareadertest
from test import crossvalidationonspecialdatasets

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(fakecrossvalidatontest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(datareadertest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(crossvalidationonspecialdatasets))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)