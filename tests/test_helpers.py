"""Compare Test Helpers

This module contains the test case for the Compare helpers module.

Usage
    python -m unittest tests.test_helpers
    python -m pytest tests/test_helpers.py
"""
import unittest
from compare.config import *
from compare.helpers import *

class CompareHelpersTest(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_dummy(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
   unittest.main()