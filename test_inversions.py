import unittest
from inversions import Inversions

class InversionsTest(unittest.TestCase):

    def test_count_sorted(self):
        items = [1, 2, 3, 4, 5]
        inv = Inversions(items)

        self.assertEqual(inv.count(), 0)

    def test_count_reversed(self):
        items = [5, 4, 3, 2, 1]
        inv = Inversions(items)

        self.assertEqual(inv.count(), 10)

    def test_count_side_inversions(self):
        items = [1, 2, 4, 3]
        inv = Inversions(items)

        # (4,3)
        self.assertEqual(inv.count(), 1)

    def test_count_split_inversions(self):
        items = [1, 4, 6, 5, 2]
        inv = Inversions(items)

        # (4,2) (6,5) (6,2) (5,2)
        self.assertEqual(inv.count(), 4)

if __name__ == '__main__':
    unittest.main()
