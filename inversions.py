#!/usr/bin/env python3
import sys

class Inversions:
    def __init__(self, items):
        self.items = items[:]
        self.inversions = 0

    # return the number of inversions
    # in the input array
    def count(self):
        left, right = 0, len(self.items) - 1
        self.__mergesort(left, right)

        return self.inversions

    def __mergesort(self, left, right):
        # base case
        if right <= left:
            return

        mid = (left + right) // 2

        # recursive calls
        self.__mergesort(left, mid)
        self.__mergesort(mid + 1, right)

        # merge sublists
        self.__merge(left, mid, right)

    def __merge(self, left, mid, right):

        # temp storage for sorted sublist
        tmp = []

        i, j = left, mid + 1

        # classic sort traversal
        while i <= mid and j <= right:
            if self.items[i] <= self.items[j]:
                tmp.append(self.items[i])
                i += 1
            else:
                tmp.append(self.items[j])
                # bump inversion count by the amount of items
                # left in the left sublist
                self.inversions += (mid - i + 1)
                j += 1

        # shift left leftovers to the right,
        # if right sublist has been exausted
        if j > right:
            last_item = mid
            move_to = right
            while last_item >= i:
                self.items[move_to] = self.items[last_item]
                move_to -= 1
                last_item -= 1

        # update items with sorted values
        idx = left
        for item in tmp:
            self.items[idx] = item
            idx += 1

if __name__ == '__main__':
    items = []
    for num in sys.stdin:
        items.append(int(num))
    inv = Inversions(items)
    del items
    print(inv.count())
