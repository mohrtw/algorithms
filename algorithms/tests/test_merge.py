import unittest
from unittest import TestCase
from algorithms.sorting.mergeSort import merge


class MergeTest(TestCase):

    def test_empty_lists(self):
        xs = merge([], [])
        self.assertEqual(xs, [])

    def test_one_empty_list(self):
        xs = merge([1], [])
        self.assertEqual(xs, [1])

        xs = merge([], [1])
        self.assertEqual(xs, [1])

    def test_one_element_lists(self):
        xs = merge([1], [2])
        self.assertEqual(xs, [1, 2])

        xs = merge([2], [1])
        self.assertEqual(xs, [1, 2])

    def test_two_element_lists(self):
        xs = merge([1, 3], [2, 4])
        self.assertEqual(xs, [1, 2, 3, 4])

        xs = merge([2, 4], [1, 3])
        self.assertEqual(xs, [1, 2, 3, 4])

    def test_different_length_lists(self):
        xs = merge([1, 4], [2, 3, 6, 7, 8])
        self.assertEqual(xs, [1, 2, 3, 4, 6, 7, 8])

        xs = merge([2, 3, 6, 7, 8], [1, 4])
        self.assertEqual(xs, [1, 2, 3, 4, 6, 7, 8])

    def test_lists_with_a_matching_element(self):
        xs = merge([1, 2], [2, 3])
        self.assertEqual(xs, [1, 2, 2, 3])

        xs = merge([2, 3], [1, 2])
        self.assertEqual(xs, [1, 2, 2, 3])

    def test_negatives(self):
        xs = merge([-2, 0, 5], [-5, 2, 3])
        self.assertEqual(xs, [-5, -2, 0, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()
