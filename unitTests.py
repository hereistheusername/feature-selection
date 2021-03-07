import unittest
from test import fakecrossvalidatontest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(fakecrossvalidatontest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)