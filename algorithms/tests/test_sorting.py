import unittest
from unittest import TestCase

from algorithms.sorting.quickSort import quickSort
from algorithms.sorting.mergeSort import mergeSort
from algorithms.sorting.insertionSort import insertionSort
from algorithms.sorting.selectionSort import selectionSort
from algorithms.sorting.bubbleSort import bubbleSort



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
            
        def test_ten_numbers(self):
            xs = sortFcn([5,13,-3,37,5,3,4,1,0,-20])
            self.assertEqual(xs,[-20,-3,0,1,3,4,5,5,13,37])
            
        def test_same_as_sorted(self):
            from random import sample
            xs = sample(range(-1000,1000),100)
            self.assertEqual(sortFcn(xs),sorted(xs))
            
            
    return sortTest
    

qsortTest = SortingTest(quickSort)
mergesortTest = SortingTest(mergeSort)
insertionSortTest = SortingTest(insertionSort)
selectionSortTest = SortingTest(selectionSort)
bubbleSortTest = SortingTest(bubbleSort)

if __name__ == '__main__':
    unittest.main()
