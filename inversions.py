#!/usr/bin/env python3

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

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                # bump inversion count by the amount of items
                # left in the left list
                self.inversions += len(left[i:])
                j += 1

        if i < len(left):
            ret.extend(left[i:])

        if j < len(right):
            ret.extend(right[j:])

        return ret
