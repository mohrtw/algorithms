import unittest
from unittest import TestCase

from algorithms.dataStructures.queue import Queue


class queue_Test(TestCase):

    def setUp(self):
        self.q = Queue()

    def test_create_queue(self):
        self.assertIsInstance(self.q, Queue)

    def test_enqueue_to_empty_queue(self):
        self.q.enqueue(1)
        self.assertEqual(1, self.q.items.head.data)
        self.assertEqual(1, self.q.items.tail.data)

    def test_enqueue_multiple_items(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue('a')

        self.assertEqual(1, self.q.items.head.data)
        self.assertEqual(2, self.q.items.head.next.data)
        self.assertEqual(3, self.q.items.tail.previous.data)
        self.assertEqual('a', self.q.items.tail.data)

    def test_dequeue_single_element_queue(self):
        self.q.enqueue(1)
        data = self.q.dequeue()

        self.assertEqual(1, data)
        self.assertIsNone(self.q.items.head)
        self.assertIsNone(self.q.items.tail)

    def test_dequeue_multiple_items(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue('a')

        data = self.q.dequeue()
        self.assertEqual(1, data)

        data = self.q.dequeue()
        self.assertEqual(2, data)

        data = self.q.dequeue()
        self.assertEqual(3, data)

        data = self.q.dequeue()
        self.assertEqual('a', data)

    def test_peek_single_element_queue(self):
        self.q.enqueue(1)
        data = self.q.peek()

        self.assertEqual(1, data)

    def test_peek_multiple_items(self):
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.q.enqueue('a')

        data = self.q.peek()
        self.assertEqual(1, data)
        self.q.dequeue()

        data = self.q.peek()
        self.assertEqual(2, data)
        self.q.dequeue()

        data = self.q.peek()
        self.assertEqual(3, data)
        self.q.dequeue()

        data = self.q.peek()
        self.assertEqual('a', data)


if __name__ == '__main__':
    unittest.main()
