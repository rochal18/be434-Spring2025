#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-02-11
Purpose: DNA: count tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('base', metavar='DNA', help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    base = args.base
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for char in base:
        if char == 'A':
            a_count = a_count + 1
        elif char == 'C':
            c_count = c_count + 1
        elif char == 'G':
            g_count = g_count + 1
        elif char == 'T':
            t_count = t_count + 1
    print(a_count, c_count, g_count, t_count)


# --------------------------------------------------
if __name__ == '__main__':
    main()
