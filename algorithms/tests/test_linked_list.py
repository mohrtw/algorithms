import unittest
from unittest import TestCase

from algorithms.dataStructures.LinkedList import Node
from algorithms.dataStructures.LinkedList import LinkedList


class linked_list_Test(TestCase):

    def test_create_node(self):
        n = Node(1)
        self.assertIsInstance(n, Node)

    def test_create_node_assigns_correct_data(self):
        n = Node(1)
        self.assertEqual(1, n.data)

    def test_create_node_assigns_None_to_next(self):
        n = Node(1)
        self.assertIsNone(n.next)

    def test_create_linked_list(self):
        ll = LinkedList()
        self.assertIsInstance(ll, LinkedList)

    def test_create_linked_list_with_node(self):
        n = Node(1)
        ll = LinkedList(n)
        self.assertEqual(n, ll.head)
        self.assertEqual(1, ll.head.data)

    def test_create_linked_list_with_multiple_nodes(self):
        n = Node(1)
        n2 = Node(2, n)
        n3 = Node('a', n2)

        ll = LinkedList(n3)
        self.assertEqual(n3, ll.head)
        self.assertEqual('a', ll.head.data)

        self.assertEqual(n2, ll.head.next)
        self.assertEqual(2, ll.head.next.data)

        self.assertEqual(n, ll.head.next.next)
        self.assertEqual(1, ll.head.next.next.data)


class get_element_Test(TestCase):

    def setUp(self):
        n = Node(1)
        n2 = Node(2, n)
        n3 = Node('a', n2)

        self.ll = LinkedList(n3)

    def test_access_first_element(self):
        n = self.ll.get_element(0)
        self.assertEqual('a', n.data)

    def test_access_second_element(self):
        n = self.ll.get_element(1)
        self.assertEqual(2, n.data)

    def test_access_third_element(self):
        n = self.ll.get_element(2)
        self.assertEqual(1, n.data)


class empty_linked_list_Test(TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_insert_end(self):
        self.ll.insert_end(1)
        self.assertEqual(1, self.ll.head.data)
        self.assertIsNone(self.ll.head.next)

    def test_insert_start(self):
        self.ll.insert_start(1)
        self.assertEqual(1, self.ll.head.data)
        self.assertIsNone(self.ll.head.next)

    def test_insert_position_0(self):
        self.ll.insert(1, 0)
        self.assertEqual(1, self.ll.head.data)
        self.assertIsNone(self.ll.head.next)


class linked_list_insert_Test(TestCase):

    def setUp(self):
        n = Node(1)
        n2 = Node(2, n)
        n3 = Node('a', n2)

        self.ll = LinkedList(n3)

    def test_insert_node_at_end(self):
        self.ll.insert_end(5)

        self.assertEqual(5, self.ll.head.next.next.next.data)
        self.assertIsNone(self.ll.head.next.next.next.next)

    def test_insert_node_at_end_doesnt_change_other_nodes(self):
        self.ll.insert_end(5)

        self.assertEqual(1, self.ll.head.next.next.data)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)

    def test_insert_node_at_start(self):
        self.ll.insert_start(5)

        self.assertEqual(5, self.ll.head.data)
        self.assertIsNotNone(self.ll.head.next)

    def test_insert_node_at_start_doesnt_change_other_nodes(self):
        self.ll.insert_start(5)

        self.assertEqual(1, self.ll.head.next.next.next.data)
        self.assertEqual(2, self.ll.head.next.next.data)
        self.assertEqual('a', self.ll.head.next.data)

    def test_insert_position_1(self):
        self.ll.insert(5, 1)

        self.assertEqual(5, self.ll.head.next.data)
        self.assertIsNotNone(self.ll.head.next.next)

    def test_insert_position_1_doesnt_change_other_nodes(self):
        self.ll.insert(5, 1)

        self.assertEqual(1, self.ll.head.next.next.next.data)
        self.assertEqual(2, self.ll.head.next.next.data)
        self.assertEqual('a', self.ll.head.data)

    def test_insert_position_2(self):
        self.ll.insert(5, 2)

        self.assertEqual(5, self.ll.head.next.next.data)
        self.assertIsNotNone(self.ll.head.next.next.next)

    def test_insert_position_2_doesnt_change_other_nodes(self):
        self.ll.insert(5, 2)

        self.assertEqual(1, self.ll.head.next.next.next.data)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)

    def test_insert_position_3(self):
        self.ll.insert(5, 3)

        self.assertEqual(5, self.ll.head.next.next.next.data)
        self.assertIsNone(self.ll.head.next.next.next.next)

    def test_insert_position_3_doesnt_change_other_nodes(self):
        self.ll.insert(5, 3)

        self.assertEqual(1, self.ll.head.next.next.data)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)


class linked_list_delete_Test(TestCase):

    def setUp(self):
        n = Node(1)
        n2 = Node(2, n)
        n3 = Node('a', n2)

        self.ll = LinkedList(n3)

    def test_delete_head(self):
        self.ll.delete(0)

        self.assertEqual(2, self.ll.head.data)
        self.assertEqual(1, self.ll.head.next.data)
        self.assertIsNone(self.ll.head.next.next)

    def test_delete_end(self):
        self.ll.delete(2)

        self.assertIsNone(self.ll.head.next.next)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)


class linked_list_print_Test(TestCase):

    def setUp(self):
        n = Node(1)
        n2 = Node(2, n)
        n3 = Node('a', n2)

        self.ll = LinkedList(n3)

    def test_display(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.ll.display()
            output = out.getvalue().strip()
            self.assertEqual(output, "a\n2\n1")
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
