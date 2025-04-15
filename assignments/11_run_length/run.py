#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-04-15
Purpose: Run length
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str', metavar='str', help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.str
    if os.path.isfile(seq):
        with open(seq, "rt", encoding="utf-8") as file:
            seq = file.read().rstrip()
    print(rle(seq))


# --------------------------------------------------
def rle(seq):
    '''Create RLE'''
    encoded = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            encoded.append(seq[i - 1] + (str(count) if count > 1 else ''))
            count = 1
    encoded.append(seq[-1] + (str(count) if count > 1 else ''))
    return ''.join(encoded)


# --------------------------------------------------
if __name__ == '__main__':
    main()
