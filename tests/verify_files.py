#!/usr/bin/env python

"""
Verify content of data files, and exit with error code 1 if it fails.
"""


from __future__ import absolute_import, print_function, unicode_literals
from itertools import islice
from os import path
import sys


ROOT_DIR = path.join(path.dirname(path.realpath(__file__)), "..")
DATA_DIR = path.join(ROOT_DIR, "data")


HEADER_NUM_LINES = 10
FOOTER_NUM_LINES = 5

FILE_CONTAINS = {
    "ReadMe.txt": [
        # Header
        "IDNA Mapping",
        "www.unicode.org/reports/tr46",
    ],
    "IdnaMappingTable.txt": [
        # Header
        "IdnaMappingTable",
        "Unicode IDNA Compatible Preprocessing",
        "www.unicode.org/reports/tr46",
        # Footer
        "# Total code points:",
    ],
}


def verify_files():
    for filepath, needles in FILE_CONTAINS.iteritems():
        with open(path.join(DATA_DIR, filepath), "r") as f:
            lines = list(f)
            header = "".join(lines[:HEADER_NUM_LINES])
            footer = "".join(lines[-FOOTER_NUM_LINES:])
            for needle in needles:
                if needle not in header and needle not in footer:
                    raise Exception("cannot find `%s` in file `%s`" %
                                    (needle, filepath))


if __name__ == '__main__':
    try:
        verify_files()
    except Exception, err:
        print("Error: %s" % err)
        sys.exit(1)
