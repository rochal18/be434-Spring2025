#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-02-05
Purpose: Divide two numbers
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divide two numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dividend',
                        help='Dividend (numerator)',
                        metavar='int',
                        type=int)

    parser.add_argument('divisor',
                        help='Divisor (denominator)',
                        metavar='int',
                        type=int)

    args = parser.parse_args()
    dividend = args.dividend
    divisor = args.divisor
    if divisor == 0:
        print('Usage: Cannot divide by zero, dum-dum!')
        sys.exit(1)
    quotient = dividend // divisor
    print(f'{dividend} / {divisor} = {quotient}')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
