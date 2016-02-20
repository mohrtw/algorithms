import unittest
from unittest import TestCase

from algorithms.dataStructures.Deque import Deque


class deque_Test(TestCase):

    def setUp(self):
        self.d = Deque()

    def test_create_deque(self):
        self.assertIsInstance(self.d, Deque)

    def test_push_to_empty_deque(self):
        self.d.push(1)
        self.assertEqual(1, self.d.items.head.data)
        self.assertEqual(1, self.d.items.tail.data)

    def test_push_multiple_items(self):
        self.d.push(1)
        self.d.push(2)
        self.d.push(3)
        self.d.push('a')

        self.assertEqual(1, self.d.items.head.data)
        self.assertEqual(2, self.d.items.head.next.data)
        self.assertEqual(3, self.d.items.tail.previous.data)
        self.assertEqual('a', self.d.items.tail.data)

    def test_inject_to_empty_deque(self):
        self.d.inject(1)
        self.assertEqual(1, self.d.items.head.data)
        self.assertEqual(1, self.d.items.tail.data)

    def test_inject_multiple_items(self):
        self.d.inject(1)
        self.d.inject(2)
        self.d.inject(3)
        self.d.inject('a')

        self.assertEqual('a', self.d.items.head.data)
        self.assertEqual(3, self.d.items.head.next.data)
        self.assertEqual(2, self.d.items.tail.previous.data)
        self.assertEqual(1, self.d.items.tail.data)

    def test_pop_single_element_deque(self):
        self.d.push(1)
        data = self.d.pop()

        self.assertEqual(1, data)
        self.assertIsNone(self.d.items.head)
        self.assertIsNone(self.d.items.tail)

    def test_pop_multiple_items(self):
        self.d.push(1)
        self.d.push(2)
        self.d.push(3)
        self.d.push('a')

        data = self.d.pop()
        self.assertEqual(1, data)

        data = self.d.pop()
        self.assertEqual(2, data)

        data = self.d.pop()
        self.assertEqual(3, data)

        data = self.d.pop()
        self.assertEqual('a', data)

    def test_eject_single_element_deque(self):
        self.d.inject(1)
        data = self.d.eject()

        self.assertEqual(1, data)
        self.assertIsNone(self.d.items.head)
        self.assertIsNone(self.d.items.tail)

    def test_eject_multiple_items(self):
        self.d.inject(1)
        self.d.inject(2)
        self.d.inject(3)
        self.d.inject('a')

        data = self.d.eject()
        self.assertEqual(1, data)

        data = self.d.eject()
        self.assertEqual(2, data)

        data = self.d.eject()
        self.assertEqual(3, data)

        data = self.d.eject()
        self.assertEqual('a', data)

    def test_peek_first_single_element_deque(self):
        self.d.push(1)
        data = self.d.peek_first()

        self.assertEqual(1, data)

    def test_peek_first_multiple_items(self):
        self.d.push(1)
        self.d.push(2)
        self.d.push(3)
        self.d.push('a')

        data = self.d.peek_first()
        self.assertEqual(1, data)
        self.d.pop()

        data = self.d.peek_first()
        self.assertEqual(2, data)
        self.d.pop()

        data = self.d.peek_first()
        self.assertEqual(3, data)
        self.d.pop()

        data = self.d.peek_first()
        self.assertEqual('a', data)

    def test_peek_last_single_element_deque(self):
        self.d.push(1)
        data = self.d.peek_last()

        self.assertEqual(1, data)

    def test_peek_last_multiple_items(self):
        self.d.push(1)
        self.d.push(2)
        self.d.push(3)
        self.d.push('a')

        data = self.d.peek_last()
        self.assertEqual('a', data)
        self.d.eject()

        data = self.d.peek_last()
        self.assertEqual(3, data)
        self.d.eject()

        data = self.d.peek_last()
        self.assertEqual(2, data)
        self.d.eject()

        data = self.d.peek_last()
        self.assertEqual(1, data)


if __name__ == '__main__':
    unittest.main()
