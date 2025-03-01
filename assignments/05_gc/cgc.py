#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-03-01
Purpose: Compute GC Content
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Compute GC Content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input sequence file',
                        nargs='?',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=sys.stdin)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    highest_gc = 0
    highest_gc_id = ""
    Id = ""
    gc = 0
    total_bases = 0
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if Id:
                if total_bases > 0:
                    gc_content = (gc / total_bases) * 100
                    if gc_content > highest_gc:
                        highest_gc = gc_content
                        highest_gc_id = Id
            Id = line[1:]
            gc = 0
            total_bases = 0
        else:
            for base in line:
                if base == 'G' or base == 'C':
                    gc += 1
                total_bases += 1
    if Id and total_bases > 0:
        gc_content = (gc / total_bases) * 100
        if gc_content > highest_gc:
            highest_gc = gc_content
            highest_gc_id = Id

    print(f"{highest_gc_id} {highest_gc:.06f}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
