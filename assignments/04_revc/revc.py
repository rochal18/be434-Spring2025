#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18>
Date   : 2025-02-19
Purpose: Print the reverse complement of DNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('DNA', metavar='str', help='Input sequence or file')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    dna = args.DNA
    if os.path.isfile(dna):
        # Use a with block and specify encoding
        with open(dna, "rt", encoding="utf-8") as file:
            dna = file.read().rstrip()
    complements = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A',
        'a': 't',
        'c': 'g',
        'g': 'c',
        't': 'a'
    }
    reverse_dna = ''
    complement_dna = ''
    for i in dna[::-1]:
        reverse_dna += i
    for j in reverse_dna:
        complement_dna += complements.get(j)
    print(complement_dna)


# --------------------------------------------------
if __name__ == '__main__':
    main()
