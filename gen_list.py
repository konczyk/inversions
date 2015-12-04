#!/usr/bin/env python3

import argparse, random

parser = argparse.ArgumentParser(description='Generate input to Inversions.')
parser.add_argument('nums', metavar='n', type=int,
                    help='upper bound number')

args = parser.parse_args()

nums = list(range(args.nums))
random.shuffle(nums)
for num in nums:
    print(num + 1)
