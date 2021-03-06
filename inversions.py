#!/usr/bin/env python3


class Inversions:
    """
    Merge sort implementation with inversions counting
    """

    def __init__(self, items, threshold = 10):
        """
        Copy the list of items and set inversions to 0
        Create tmp list of the same size as items to hold merge data
        Set default threshold to switch to insertion sort
        """

        self._items = list(items)
        self._tmp = [0] * len(self._items)
        self._inversions = 0
        self._threshold = threshold

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

        # switch to insertion sort for small subarrays
        if right - left <= self._threshold:
            self._insertion_sort(left, right)
        else:
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

        # copy subarrays being merged into the tmp list
        self._tmp[left:right+1] = self._items[left:right+1]

        i, j, k = left, mid + 1, left
        # loop until we visit all the values from left to right
        while k <= right:
            # left subarray is exausted
            if i > mid:
                self._items[k] = self._tmp[j]
                j += 1
            # right subarray is exausted
            elif j > right:
                self._items[k] = self._tmp[i]
                i += 1
            # compare and copy
            elif self._tmp[j] < self._tmp[i]:
                self._items[k] = self._tmp[j]
                j += 1
                # bump inversions counter by the number of items
                # still not merged from the left subarray
                self._inversions += (mid - i + 1)
            else:
                self._items[k] = self._tmp[i]
                i += 1

            k += 1

    def _insertion_sort(self, left, right):
        """
        Sort subarrays indicated by the passed boundaries using
        insertion sort algorithm
        """
        i = left
        while i <= right:
            j = i
            while j > left and self._items[j] < self._items[j-1]:
                # swap items
                self._items[j-1], self._items[j] = self._items[j], self._items[j-1]
                self._inversions += 1
                j -= 1
            i += 1
