import unittest
from unittest import TestCase, skip

from algorithms.dataStructures.DoublyLinkedList import DoublyLinkedNode
from algorithms.dataStructures.DoublyLinkedList import DoublyLinkedList


class doubly_linked_list_creation_Test(TestCase):

    def test_create_node(self):
        n = DoublyLinkedNode(1)
        self.assertIsInstance(n, DoublyLinkedNode)

    def test_create_node_assigns_correct_data(self):
        n = DoublyLinkedNode(1)
        self.assertEqual(1, n.data)

    def test_create_node_assigns_None_to_next(self):
        n = DoublyLinkedNode(1)
        self.assertIsNone(n.next)

    def test_create_node_assigns_None_to_previous(self):
        n = DoublyLinkedNode(1)
        self.assertIsNone(n.previous)

    def test_create_linked_list(self):
        ll = DoublyLinkedList()
        self.assertIsInstance(ll, DoublyLinkedList)

    def test_create_linked_list_with_one_node(self):
        n = DoublyLinkedNode(1)
        ll = DoublyLinkedList(n)
        self.assertEqual(n, ll.head)
        self.assertEqual(1, ll.head.data)
        self.assertEqual(n, ll.tail)
        self.assertEqual(1, ll.tail.data)

    def test_create_linked_list_with_tail_node(self):
        n = DoublyLinkedNode(1)
        ll = DoublyLinkedList(None, n)
        self.assertEqual(n, ll.tail)
        self.assertEqual(1, ll.tail.data)
        self.assertIsNone(ll.head)

    def test_create_linked_list_with_multiple_nodes(self):
        n = DoublyLinkedNode(1)
        n2 = DoublyLinkedNode(2, n)
        n3 = DoublyLinkedNode('a', n2)

        ll = DoublyLinkedList(n3)
        self.assertEqual(n3, ll.head)
        self.assertEqual('a', ll.head.data)

        self.assertEqual(n2, ll.head.next)
        self.assertEqual(2, ll.head.next.data)

        self.assertEqual(n, ll.head.next.next)
        self.assertEqual(1, ll.head.next.next.data)


class get_element_Test(TestCase):

    def setUp(self):
        n = DoublyLinkedNode(1)
        n2 = DoublyLinkedNode(2, n)
        n3 = DoublyLinkedNode('a', n2)

        self.ll = DoublyLinkedList(n3)

    def test_access_first_element(self):
        n = self.ll.get_element(0)
        self.assertEqual('a', n.data)

    def test_access_second_element(self):
        n = self.ll.get_element(1)
        self.assertEqual(2, n.data)

    def test_access_third_element(self):
        n = self.ll.get_element(2)
        self.assertEqual(1, n.data)

    def test_get_head_single_element_list(self):
        n = DoublyLinkedNode(1)
        dll = DoublyLinkedList(n)

        data = dll.get_head()

        self.assertEqual(n, data)

    def test_get_head_multiple_element_list(self):
        n = self.ll.get_head()

        self.assertEqual('a', n.data)

    def test_get_tail_single_element_list(self):
        n = DoublyLinkedNode(1)
        dll = DoublyLinkedList(n)

        data = dll.get_tail()

        self.assertEqual(n, data)

    def test_get_tail_multiple_element_list(self):
        n = self.ll.get_tail()

        self.assertEqual(1, n.data)


class empty_doubly_linked_list_Test(TestCase):

    def setUp(self):
        self.ll = DoublyLinkedList()

    def test_insert_end(self):
        self.ll.insert_end(1)
        self.assertEqual(1, self.ll.head.data)
        self.assertEqual(1, self.ll.tail.data)
        self.assertIsNone(self.ll.head.next)

    def test_insert_end_tail_is_updated(self):
        self.ll.insert_end(1)
        self.assertEqual(1, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)

    def test_insert_start(self):
        self.ll.insert_start(1)
        self.assertEqual(1, self.ll.head.data)
        self.assertIsNone(self.ll.head.next)

    def test_insert_start_tail_is_updated(self):
        self.ll.insert_start(1)
        self.assertEqual(1, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)

    def test_insert_position_0(self):
        self.ll.insert(1, 0)
        self.assertEqual(1, self.ll.head.data)
        self.assertIsNone(self.ll.head.next)

    def test_insert_position_0_tail_is_updated(self):
        self.ll.insert(1, 0)
        self.assertEqual(1, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)


class doubly_linked_list_insert_Test(TestCase):

    def setUp(self):
        n = DoublyLinkedNode(1)
        n2 = DoublyLinkedNode(2, n)
        n3 = DoublyLinkedNode('a', n2)

        self.ll = DoublyLinkedList(n3)

    def test_insert_node_at_end(self):
        self.ll.insert_end(5)

        self.assertEqual(5, self.ll.head.next.next.next.data)
        self.assertIsNone(self.ll.head.next.next.next.next)
        self.assertEqual(5, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)
        self.assertEqual(1, self.ll.tail.previous.data)

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
        self.assertEqual(1, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)
        self.assertEqual(2, self.ll.tail.previous.data)

    def test_insert_position_1(self):
        self.ll.insert(5, 1)

        self.assertEqual(5, self.ll.head.next.data)
        self.assertIsNotNone(self.ll.head.next.next)

    def test_insert_position_1_doesnt_change_other_nodes(self):
        self.ll.insert(5, 1)

        self.assertEqual(1, self.ll.head.next.next.next.data)
        self.assertEqual(2, self.ll.head.next.next.data)
        self.assertEqual('a', self.ll.head.data)
        self.assertEqual(1, self.ll.tail.data)

    def test_insert_position_1_correct_previous(self):
        self.ll.insert(5, 1)
        # 'a' 5 2 1

        self.assertEqual(2, self.ll.head.next.next.next.previous.data)
        self.assertEqual(5, self.ll.head.next.next.previous.data)
        self.assertEqual('a', self.ll.head.next.previous.data)
        self.assertEqual(2, self.ll.tail.previous.data)

    def test_insert_position_2(self):
        self.ll.insert(5, 2)

        self.assertEqual(5, self.ll.head.next.next.data)
        self.assertIsNotNone(self.ll.head.next.next.next)

    def test_insert_position_2_doesnt_change_other_nodes(self):
        self.ll.insert(5, 2)

        self.assertEqual(1, self.ll.head.next.next.next.data)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)
        self.assertEqual(1, self.ll.tail.data)

    def test_insert_position_2_correct_previous(self):
        self.ll.insert(5, 2)
        # 'a' 2 5 1

        self.assertEqual(5, self.ll.head.next.next.next.previous.data)
        self.assertEqual(2, self.ll.head.next.next.previous.data)
        self.assertEqual('a', self.ll.head.next.previous.data)
        self.assertEqual(5, self.ll.tail.previous.data)

    def test_insert_position_3(self):
        self.ll.insert(5, 3)

        self.assertEqual(5, self.ll.head.next.next.next.data)
        self.assertIsNone(self.ll.head.next.next.next.next)
        self.assertEqual(5, self.ll.tail.data)

    def test_insert_position_3_doesnt_change_other_nodes(self):
        self.ll.insert(5, 3)

        self.assertEqual(1, self.ll.head.next.next.data)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)

    def test_insert_position_3_correct_previous(self):
        self.ll.insert(5, 3)
        # 'a' 2 1 5

        self.assertEqual(1, self.ll.head.next.next.next.previous.data)
        self.assertEqual(2, self.ll.head.next.next.previous.data)
        self.assertEqual('a', self.ll.head.next.previous.data)
        self.assertEqual(1, self.ll.tail.previous.data)


class doubly_linked_list_delete_Test(TestCase):

    def setUp(self):
        n = DoublyLinkedNode(1)
        n2 = DoublyLinkedNode(2, n)
        n3 = DoublyLinkedNode('a', n2)
        # 'a' 2 1

        self.ll = DoublyLinkedList(n3)

    def test_delete_only_element(self):
        dll = DoublyLinkedList()
        dll.insert_start(1)
        dll.delete(0)

        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_delete_start(self):
        self.ll.delete(0)

        self.assertEqual(2, self.ll.head.data)
        self.assertEqual(1, self.ll.head.next.data)
        self.assertIsNone(self.ll.head.next.next)
        self.assertEqual(1, self.ll.tail.data)

    def test_delete_start_correct_previous(self):
        self.ll.delete(0)

        self.assertEqual(2, self.ll.head.next.previous.data)
        self.assertEqual(2, self.ll.tail.previous.data)
        self.assertIsNone(self.ll.head.previous)

    def test_delete_middle(self):
        self.ll.delete(1)

        self.assertIsNone(self.ll.head.next.next)
        self.assertEqual(1, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)
        self.assertEqual(1, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)

    def test_delete_middle_correct_previous(self):
        self.ll.delete(1)

        self.assertEqual('a', self.ll.head.next.previous.data)
        self.assertEqual('a', self.ll.tail.previous.data)
        self.assertIsNone(self.ll.head.previous)

    def test_delete_end(self):
        self.ll.delete(2)

        self.assertIsNone(self.ll.head.next.next)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)
        self.assertEqual(2, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)

    def test_delete_end_correct_previous(self):
        self.ll.delete(2)

        self.assertEqual('a', self.ll.head.next.previous.data)
        self.assertEqual('a', self.ll.tail.previous.data)
        self.assertIsNone(self.ll.head.previous)

    def test_delete_head_single_element(self):
        dll = DoublyLinkedList()
        dll.insert_start(1)
        dll.delete_head()

        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_delete_head_multiple_elements(self):
        self.ll.delete_head()

        self.assertEqual(2, self.ll.head.data)
        self.assertEqual(1, self.ll.head.next.data)
        self.assertIsNone(self.ll.head.next.next)
        self.assertEqual(1, self.ll.tail.data)

        self.assertEqual(2, self.ll.head.next.previous.data)
        self.assertEqual(2, self.ll.tail.previous.data)
        self.assertIsNone(self.ll.head.previous)

    def test_delete_tail_single_element(self):
        dll = DoublyLinkedList()
        dll.insert_start(1)
        dll.delete_tail()

        self.assertIsNone(dll.head)
        self.assertIsNone(dll.tail)

    def test_delete_tail_multiple_elements(self):
        self.ll.delete_tail()

        self.assertIsNone(self.ll.head.next.next)
        self.assertEqual(2, self.ll.head.next.data)
        self.assertEqual('a', self.ll.head.data)
        self.assertEqual(2, self.ll.tail.data)
        self.assertIsNone(self.ll.tail.next)

        self.assertEqual('a', self.ll.head.next.previous.data)
        self.assertEqual('a', self.ll.tail.previous.data)
        self.assertIsNone(self.ll.head.previous)


class doubly_linked_list_print_Test(TestCase):

    def setUp(self):
        n = DoublyLinkedNode(1)
        n2 = DoublyLinkedNode(2, n)
        n3 = DoublyLinkedNode('a', n2)

        self.ll = DoublyLinkedList(n3)

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
