#!/usr/bin/env python

"""
Verify content of data files, and exit with error code 1 if it fails.
"""


from __future__ import absolute_import, print_function, unicode_literals
from itertools import islice
from os import path
import sys


ROOT_DIR = path.join(path.dirname(path.realpath(__file__)), "..", "..")
DATA_DIR = path.join(ROOT_DIR, "idna")


HEADER_NUM_LINES = 10
FOOTER_NUM_LINES = 5

FILE_CONTAINS = {
    "ReadMe.txt": [
        # Header
        "www.unicode.org/reports/tr46",
    ],
    "IdnaMappingTable.txt": [
        # Header
        "IdnaMappingTable",
        "www.unicode.org/reports/tr46",
        # Footer
        "# Total code points:",
    ],
    "IdnaTest.txt": [
        # Header
        "IdnaTest",
        "www.unicode.org/reports/tr46",
    ],
}


def verify_files():
    for filepath, needles in FILE_CONTAINS.iteritems():
        print("Verfitying: %s" % filepath)
        with open(path.join(DATA_DIR, filepath), "r") as f:
            lines = list(f)
            header = "".join([x.decode('utf-8') for x in lines[:HEADER_NUM_LINES]])
            footer = "".join([x.decode('utf-8') for x in lines[-FOOTER_NUM_LINES:]])
            for needle in needles:
                if needle not in header and needle not in footer:
                    raise Exception("cannot find `%s` in file `%s`" %
                                    (needle, filepath))


if __name__ == '__main__':
    verify_files()
