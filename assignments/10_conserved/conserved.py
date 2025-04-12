#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-04-12
Purpose: Find conserved sequence
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.FILE
    seqs = []
    for line in file.readlines():
        seqs.append(line.strip())
    for seq in seqs:
        print(seq)
    conserved = []
    for i in range(len(seqs[0])):
        bases = [seq[i] for seq in seqs]
        if len(set(bases)) == 1:
            conserved.append('|')
        else:
            conserved.append('X')
    print(''.join(conserved))


# --------------------------------------------------
if __name__ == '__main__':
    main()
