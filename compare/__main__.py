"""Compare Main

This module contains the entry point code for the Compare program.
"""
from compare.arg_parser import create_parser
from compare.compare import Compare

def main():
    parser = create_parser()

    args = parser.parse_args()

    options = vars(args)

    compare = Compare(parser, options)

    print(repr(compare))

    return compare

if __name__ == '__main__':
    main()