import unittest
import classification_test
import test_suite
from util import delete_files

# try to load all testcases from given module, hope your testcases are extending from unittest.TestCase
suite1 = unittest.TestLoader().loadTestsFromModule(classification_test)
# run all tests with verbosity
unittest.TextTestRunner(verbosity=2).run(suite1)

# try to load all testcases from given module, hope your testcases are extending from unittest.TestCase
suite2 = unittest.TestLoader().loadTestsFromModule(test_suite)
# run all tests with verbosity
unittest.TextTestRunner(verbosity=2).run(suite2)

delete_files()

print('---------------------------------------------Test suite completed----------------------------------------------')
