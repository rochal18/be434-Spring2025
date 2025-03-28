#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-03-28
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('FILE2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def get_words(filehandle):
    """Get words from files"""

    words = set()
    for line in filehandle:
        line = line.strip()
        line_words = line.split()
        for word in line_words:
            words.add(word)
    return words


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    outfile = args.outfile
    file1 = args.FILE1
    file2 = args.FILE2
    words1 = get_words(file1)
    words2 = get_words(file2)
    common_words = sorted(words1 & words2)
    for word in common_words:
        print(word, file=outfile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
