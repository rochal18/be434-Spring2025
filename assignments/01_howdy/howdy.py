#!/usr/bin/env python3
"""
Author : Lorenzo Rocha <lorenzoarocha18@arizona.edu>
Date   : 2025-01-22
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')
    parser.add_argument('-n',
                        '--name',
                        help='Name to greet',
                        metavar='str',
                        type=str,
                        default="Stranger")
    parser.add_argument('-e',
                        '--excited',
                        help='Include an exclamation point',
                        default=False,
                        action='store_true')
    args = parser.parse_args()
    greeting = args.greeting
    name = args.name
    excited = "!" if args.excited else "."
    print(greeting + ', ' + name + excited)
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    get_args()
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
