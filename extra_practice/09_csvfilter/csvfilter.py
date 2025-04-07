#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-04-04
Purpose: Filter delimited records
"""

import argparse
import csv
import os
import sys
import re
import subprocess


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        help='Column name for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        metavar='delim',
                        type=str,
                        help='Input delimiter',
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Filter the file"""

    args = get_args()
    try:      
        reader = csv.DictReader(args.file, delimiter=args.delimiter)
        if args.col and args.col not in reader.fieldnames:
            print(f'--col "{args.col}" not a valid column!')
            print(f"Choose from {', '.join(reader.fieldnames)}")
            sys.exit(1)
        writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        num_written = 0
        search_col = args.col
        search_for = args.val
        for rec in reader:
            text = rec.get(search_col) if search_col else ' '.join(rec.values())
            if re.search(search_for, text, re.IGNORECASE):
                num_written += 1
                writer.writerow(rec)
        print('Done, wrote',num_written, 'to "'+ args.outfile.name + '".')   
    except FileNotFoundError:
        print('Error: The file ',args.file.name,'was not found.')
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()