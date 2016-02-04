from algorithms.sorting.sorting import quickSort

import unittest

from unittest import TestCase

class QuickSortTest(TestCase):    
    
    def test_empty_list(self):
        xs = quickSort([])
        self.assertEqual(xs,[])

    def test_single_item(self):
        xs = quickSort([1])
        self.assertEqual(xs,[1])
        
    def test_two_numbers(self):
        xs = quickSort([2,1])
        self.assertEqual(xs, [1,2])
        
        xs = quickSort([2,1])
        self.assertEqual(xs, [1,2])
        
    def test_two_identical_numbers(self):
        xs = quickSort([2,2])
        self.assertEqual(xs, [2,2])
        
        xs = quickSort([0,0])
        self.assertEqual(xs, [0,0])
        
        xs = quickSort([-3,-3])
        self.assertEqual(xs, [-3,-3])
        
    def test_two_numbers_one_negative(self):
        xs = quickSort([-2,1])
        self.assertEqual(xs, [-2,1])
        
        xs = quickSort([1,-2])
        self.assertEqual(xs, [-2,1])
        
    def test_two_negative_numbers(self):
        xs = quickSort([-2,-4])
        self.assertEqual(xs, [-4,-2])
        
        xs = quickSort([-4,-2])
        self.assertEqual(xs, [-4,-2])
        
    def test_three_numbers(self):
        xs = quickSort([0,1,2])
        self.assertEqual(xs,[0,1,2])
        
        xs = quickSort([0,2,1])
        self.assertEqual(xs,[0,1,2])
        
        xs = quickSort([1,0,2])
        self.assertEqual(xs, [0,1,2])
        
        xs = quickSort([1,2,0])
        self.assertEqual(xs, [0,1,2])
        
        xs = quickSort([2,0,1])
        self.assertEqual(xs, [0,1,2])
        
        xs = quickSort([2,1,0])
        self.assertEqual(xs, [0,1,2])

if __name__ == '__main__':
    unittest.main()
