#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-05-06
Purpose: Caesar shift
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Output file',
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def sub_table(number, decode=False):
    """Substitution dictionary"""

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted = alpha[number:] + alpha[:number]
    subs = {}
    if decode:
        for i, letter in enumerate(shifted):
            subs[letter] = alpha[i]
    else:
        for i, letter in enumerate(alpha):
            subs[letter] = shifted[i]

    return subs


# ---------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    subs = sub_table(args.number % 26, args.decode)
    for line in args.FILE:
        new_line = ''
        for char in line:
            if char.isalpha():
                new_line += subs.get(char.upper(), char.upper())
            else:
                new_line += char
        print(new_line.upper(), file=args.outfile, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
