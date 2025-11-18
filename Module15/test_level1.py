import unittest
import random


class MergerSorter():
    def merge_sort(self, a):
        if len(a) < 2:
            return a[:]
        else:
            median = int(len(a) / 2)
            left = self.merge_sort(a[:median])
            right = self.merge_sort(a[median:])
            return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        while i < len(left):
            res.append(left[i])
            i += 1
        while j < len(right):
            res.append(right[j])
            j += 1
        return res


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.array_to_sort = [random.randint(1, 200) for i in range(200)]
        self.merger = MergerSorter()

    def test_sorting(self):
        original_array = self.array_to_sort[:]

        sorted_by_algorithm = self.merger.merge_sort(self.array_to_sort)

        original_array.sort()

        self.assertEqual(sorted_by_algorithm, original_array)


if __name__ == "__main__":
    unittest.main()