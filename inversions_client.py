#!/usr/bin/env python3

import argparse
import random
import sys
from inversions import Inversions

parser = argparse.ArgumentParser(description='Inversions client.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-b', '--bound', type=int, help='Upper bound number')
group.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                   default=sys.stdin,
                   help='Input file with numbers (default stdin)')

args = parser.parse_args()
if args.bound is not None:
    nums = list(range(1, args.bound+1))
    random.shuffle(nums)
else:
    nums = [int(num) for num in args.infile]

inv = Inversions(nums)
print(inv.count())
