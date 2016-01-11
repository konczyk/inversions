#!/usr/bin/env python3

import unittest
from inversions import Inversions

class InversionsTest(unittest.TestCase):

    def test_count_sorted(self):
        items = [1, 2, 3, 4, 5]

        # merge sort only
        inv = Inversions(items, 0)
        self.assertEqual(inv.count(), 0)

        # insertion sort only
        inv = Inversions(items)
        self.assertEqual(inv.count(), 0)

        # mixed
        inv = Inversions(items, 2)
        self.assertEqual(inv.count(), 0)

    def test_count_reversed(self):
        items = [5, 4, 3, 2, 1]

        # merge sort only
        inv = Inversions(items, 0)
        self.assertEqual(inv.count(), 10)

        # insertion sort only
        inv = Inversions(items)
        self.assertEqual(inv.count(), 10)

        # mixed
        inv = Inversions(items, 2)
        self.assertEqual(inv.count(), 10)

    def test_count_side_inversions(self):
        items = [1, 2, 4, 3]
        # (4,3)

        # merge sort only
        inv = Inversions(items, 0)
        self.assertEqual(inv.count(), 1)

        # insertion sort only
        inv = Inversions(items)
        self.assertEqual(inv.count(), 1)

        # mixed
        inv = Inversions(items, 2)
        self.assertEqual(inv.count(), 1)

    def test_count_split_inversions(self):
        items = [1, 4, 6, 5, 2]
        # (4,2) (6,5) (6,2) (5,2)

        # merge sort only
        inv = Inversions(items, 0)
        self.assertEqual(inv.count(), 4)

        # insertion sort only
        inv = Inversions(items)
        self.assertEqual(inv.count(), 4)

        # mixed
        inv = Inversions(items, 2)
        self.assertEqual(inv.count(), 4)

if __name__ == '__main__':
    unittest.main()
