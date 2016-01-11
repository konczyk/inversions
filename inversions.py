#!/usr/bin/env python3
import sys

class Inversions:
    """
    Merge sort implementation with inversions counting
    """

    def __init__(self, items):
        """
        Copy the list of items and set inversions to 0
        """

        self._items = items[:]
        self._inversions = 0

    def count(self):
        """
        Count the number of inversions using merge sort and
        return the result
        """

        left, right = 0, len(self._items) - 1
        self._sort(left, right)

        return self._inversions

    def _sort(self, left, right):
        """
        Sort the array by recursive split using the passed boundaries
        """

        # base case
        if right <= left:
            return

        mid = (left + right) // 2

        # recursive calls
        self._sort(left, mid)
        self._sort(mid + 1, right)

        # merge step
        self._merge(left, mid, right)

    def _merge(self, left, mid, right):
        """
        Merge subarrays indicated by the passed boundaries
        """

        # temp storage for sorted sublist
        tmp = []

        i, j = left, mid + 1

        # classic sort traversal
        while i <= mid and j <= right:
            if self._items[i] <= self._items[j]:
                tmp.append(self._items[i])
                i += 1
            else:
                tmp.append(self._items[j])
                # bump inversion count by the amount of items
                # left in the left sublist
                self._inversions += (mid - i + 1)
                j += 1

        # shift left leftovers to the right,
        # if right sublist has been exausted
        if j > right:
            last_item = mid
            move_to = right
            while last_item >= i:
                self._items[move_to] = self._items[last_item]
                move_to -= 1
                last_item -= 1

        # update items with sorted values
        idx = left
        for item in tmp:
            self._items[idx] = item
            idx += 1

if __name__ == '__main__':
    items = []
    for num in sys.stdin:
        items.append(int(num))
    inv = Inversions(items)
    del items
    print(inv.count())
