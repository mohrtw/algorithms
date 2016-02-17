import unittest
from unittest import TestCase

from algorithms.dataStructures.stack import Stack


class stackTest(TestCase):

    def setUp(self):
        self.s = Stack()

    def test_add_item_to_stack(self):
        item = 1
        self.s.push(item)
        self.assertEqual(item, self.s.items[0])

    def test_add_multiple_items_to_stack(self):
        self.s.push(1)
        self.s.push('a')
        self.s.push(5)
        self.s.push(1)
        self.assertEqual(1, self.s.items[0])
        self.assertEqual('a', self.s.items[1])
        self.assertEqual(5, self.s.items[2])
        self.assertEqual(1, self.s.items[3])

    def test_pop_item_from_stack(self):
        self.s.push(1)
        self.assertEqual(1, self.s.pop())

    def test_pop_multiple_items_to_stack(self):
        self.s.push(1)
        self.s.push('a')
        self.s.push(5)
        self.s.push(1)
        self.assertEqual(1, self.s.pop())
        self.assertEqual(5, self.s.pop())
        self.assertEqual('a', self.s.pop())
        self.assertEqual(1, self.s.pop())

    def test_push_push_pop_push(self):
        self.s.push(34)
        self.s.push(7)
        self.assertEqual(34, self.s.items[0])
        self.assertEqual(7, self.s.items[1])

        self.assertEqual(7, self.s.pop())
        self.s.push(4)
        self.assertEqual(4, self.s.items[1])

if __name__ == '__main__':
    unittest.main()
