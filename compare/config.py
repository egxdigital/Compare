"""Compare Config

This module contains the config definitions for the Compare program.
"""
from pathlib import Path, PurePath

ROOT=Path(__file__).resolve().parent.parent
PKG = Path(__file__).resolve().parent
DATA=Path(PurePath(ROOT, 'data'))
STATIC=Path(PurePath(ROOT, 'static'))
TESTS=Path(PurePath(ROOT, 'tests'))
TEST_DATA=Path(PurePath(TESTS, 'data'))

class ERROR():
    bad_command ='invalid command!'
    bad_directory ='invalid destination directory!'
    bad_file ='invalid input file!'

class colors():
    HEADER ='\033[95m'
    OKBLUE ='\033[94m'
    OKCYAN ='\033[96m'
    OKGREEN ='\033[92m'
    WARNING ='\033[93m'
    FAIL ='\033[91m'
    ENDC ='\033[0m'
    BOLD ='\033[1m'
    UNDERLINE ='\033[4m'
