import argparse

def create_parser():
    parser = argparse.ArgumentParser(
        prog='compare',
        fromfile_prefix_chars='@',
        usage='compare <command> [options] <partname>=<value>',
        description='Configure parts into components and perform comparisons',
        epilog='Compare it!')

    parser.add_argument('-d', '--detail',
                           action='store',
                           type=str,
                           required=False,
                           help='modifies something')
    
    parser.add_argument("-c", "--component",
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

    return parser