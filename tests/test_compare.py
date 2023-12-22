"""Test Compare

This module contains the test case for the Compare program.

Usage
    python -m unittest tests.test_compare
"""
import unittest
import argparse

from compare.config import *
from compare.helpers import *
from compare.compare import *


class CompareTest(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(
            prog='compare',
            fromfile_prefix_chars='@',
            usage='compare [options] <command> <arg1>',
            description='<desc>',
            epilog='Build it!')

        parser.add_argument('-d', '--detail',
                       action='store',
                       type=str,
                       required=False,
                       help='modifies something')
        parser.add_argument('commands',
                       nargs='+',
                       help="use a command eg. init or start")

        self.parser = parser

        def run_command(command: argparse.Namespace):
            args = command
            options = vars(args)
            compare = Compare(self.parser, options)
            return compare

        self.run_command = run_command

    def tearDown(self):
        pass

    def test_compare_command(self):
        command = argparse.Namespace(
            commands=['do', 'argument']
        )
        compare = self.run_command(command)


if __name__ == '__main__':
    unittest.main()