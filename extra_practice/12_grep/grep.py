#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-04-25
Purpose: Python grep
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pattern = re.compile(args.pattern,
                         re.IGNORECASE if args.insensitive else 0)
    files = len(args.files) > 1
    for file in args.files:
        for line in file:
            if pattern.search(line):
                prefix = file.name + ':' if files else ''
                print(prefix + line, end='', file=args.outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
