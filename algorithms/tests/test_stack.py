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

    def test_is_empty_on_empty_stack(self):
        self.assertTrue(self.s.is_empty())

    def test_is_empty_on_single_item(self):
        self.s.push(1)
        self.assertFalse(self.s.is_empty())

    def test_is_empty_on_multiple_items(self):
        self.s.push(1)
        self.s.push('a')
        self.s.push(5)
        self.assertFalse(self.s.is_empty())

    def test_peek_single_element_queue(self):
        self.s.push(1)
        data = self.s.peek()

        self.assertEqual(1, data)

    def test_peek_multiple_items(self):
        self.s.push(1)
        self.s.push(2)
        self.s.push(3)
        self.s.push('a')

        data = self.s.peek()
        self.assertEqual('a', data)
        self.s.pop()

        data = self.s.peek()
        self.assertEqual(3, data)
        self.s.pop()

        data = self.s.peek()
        self.assertEqual(2, data)
        self.s.pop()

        data = self.s.peek()
        self.assertEqual(1, data)


class createStacksTest(TestCase):

    def test_create_empty_stack(self):
        self.stk = Stack()

        self.assertIsInstance(self.stk, Stack)
        self.assertEqual(self.stk.items, [])

    def test_create_stack_with_one_element(self):
        self.stk = Stack([1])

        self.assertIsInstance(self.stk, Stack)
        self.assertEqual(self.stk.items, [1])


    def test_create_stack_with_two_elements(self):
        self.stk = Stack([1, 2])

        self.assertIsInstance(self.stk, Stack)
        self.assertEqual(self.stk.items, [1, 2])

if __name__ == '__main__':
    unittest.main()
