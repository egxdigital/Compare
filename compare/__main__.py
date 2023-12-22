"""Compare Main

This module contains the entry point code for the Compare program.
"""
import argparse
from fastapi import FastAPI
from compare.compare import Compare

def main():
    parser = argparse.ArgumentParser(
        prog='compare',
        fromfile_prefix_chars='@',
        usage='compare [options] <command> <arg1>',
        description=f'{repr(FastAPI)}',
        epilog='Compare it!!!')

    # Add arguments here

    parser.add_argument('-d', '--detail',
                           action='store',
                           type=str,
                           required=False,
                           help='modifies something')
    
    parser.add_argument("-c", "--components",
                        metavar="KEY=VALUE",
                        action='append',
                        nargs='+',
                        help="Set a number of key-value pairs "
                             "(do not put spaces before or after the = sign). "
                             "If a value contains spaces, you should define "
                             "it with double quotes: "
                             'foo="this is a sentence". Note that '
                             "values are always treated as strings.")
    
    parser.add_argument('commands',
                           nargs='+',
                           help="use a command eg. init or start")

    args = parser.parse_args()

    options = vars(args)

    compare = Compare(parser, options)

    print(repr(compare))
    print(compare)

if __name__ == '__main__':
    main()