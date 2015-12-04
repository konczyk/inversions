#!/usr/bin/env python3
import sys

class Inversions:
    def __init__(self, items):
        self.items = items;
        self.inversions = 0

    # return the number of inversions
    # in the input array
    def count(self):
        self.__mergesort(self.items)

        return self.inversions

    def __mergesort(self, items):
        if len(items) <= 1:
            return items

        mid   = len(items) // 2
        left  = self.__mergesort(items[:mid])
        right = self.__mergesort(items[mid:])

        return self.__merge(left, right)

    def __merge(self, left, right):

        ret = []
        i, j = 0, 0
        ilen, jlen = len(left), len(right)

        while i < ilen and j < jlen:
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                # bump inversion count by the amount of items
                # left in the left list
                self.inversions += len(left[i:])
                j += 1

        if i < ilen:
            ret.extend(left[i:])

        if j < jlen:
            ret.extend(right[j:])

        return ret

if __name__ == '__main__':
    items = []
    for num in sys.stdin:
        items.append(int(num))
    inv = Inversions(items)
    print(inv.count())
