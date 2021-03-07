import unittest
from test import fakecrossvalidatontest
from test import datareadertest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(fakecrossvalidatontest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(datareadertest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)