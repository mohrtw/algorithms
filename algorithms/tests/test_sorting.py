import unittest
from unittest import TestCase

from algorithms.sorting.quickSort import quickSort

from algorithms.sorting.mergeSort import mergeSort

from algorithms.sorting.insertionSort import insertionSort


def SortingTest(sortFcn):
    
    class sortTest(TestCase):
    
        def test_empty_list(self):
            xs = sortFcn([])
            self.assertEqual(xs,[])
    
        def test_single_item(self):
            xs = sortFcn([1])
            self.assertEqual(xs,[1])
            
        def test_two_numbers(self):
            xs = sortFcn([2,1])
            self.assertEqual(xs, [1,2])
            
            xs = sortFcn([2,1])
            self.assertEqual(xs, [1,2])
            
        def test_two_identical_numbers(self):
            xs = sortFcn([2,2])
            self.assertEqual(xs, [2,2])
            
            xs = sortFcn([0,0])
            self.assertEqual(xs, [0,0])
            
            xs = sortFcn([-3,-3])
            self.assertEqual(xs, [-3,-3])
            
        def test_two_numbers_one_negative(self):
            xs = sortFcn([-2,1])
            self.assertEqual(xs, [-2,1])
            
            xs = sortFcn([1,-2])
            self.assertEqual(xs, [-2,1])
            
        def test_two_negative_numbers(self):
            xs = sortFcn([-2,-4])
            self.assertEqual(xs, [-4,-2])
            
            xs = sortFcn([-4,-2])
            self.assertEqual(xs, [-4,-2])
            
        def test_three_numbers(self):
            xs = sortFcn([0,1,2])
            self.assertEqual(xs,[0,1,2])
            
            xs = sortFcn([0,2,1])
            self.assertEqual(xs,[0,1,2])
            
            xs = sortFcn([1,0,2])
            self.assertEqual(xs, [0,1,2])
            
            xs = sortFcn([1,2,0])
            self.assertEqual(xs, [0,1,2])
            
            xs = sortFcn([2,0,1])
            self.assertEqual(xs, [0,1,2])
            
            xs = sortFcn([2,1,0])
            self.assertEqual(xs, [0,1,2])
            
    return sortTest
    

qsortTest = SortingTest(quickSort)

mergesortTest = SortingTest(mergeSort)
insertionSortTest = SortingTest(insertionSort)

if __name__ == '__main__':
    unittest.main()
