#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-03-07
Purpose: DNA to RNA
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Compute GC Content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input sequence file',
                        nargs='*',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--out_dir',
                        help='Output directory',
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out = args.out_dir
    if not args.file:
        print("Usage:", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)
    file_count = 0
    sequence_count = 0
    for file in args.file:
        file_count += 1
        file_name = os.path.basename(file.name)
        file_content = file.read().rstrip()
        sequence = file_content.splitlines()
        sequence_count += len(sequence)
        complement_rna = file_content.replace('T', 'U')
        output_file_path = os.path.join(out, file_name)
        with open(output_file_path, 'w', encoding="utf-8") as output_file:
            output_file.write(complement_rna)
    seq_word = "sequence" if sequence_count == 1 else "sequences"
    file_word = "file" if file_count == 1 else "files"
    print('Done, wrote', sequence_count, seq_word, 'in', file_count, file_word,
          'to directory "' + out + '".')
    sys.exit(0)


# --------------------------------------------------
if __name__ == '__main__':
    main()
