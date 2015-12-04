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
        return items

    def __merge(self, left, right):
        return []
