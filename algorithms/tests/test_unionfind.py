import unittest
from unittest import TestCase

from algorithms.dataStructures.UnionFind import Node, UnionFind

class emptyTest(TestCase):

    def setUp(self):
        self.nodes = set()
        self.uf = UnionFind(self.nodes)

    def test_nodes_is_empty(self):
        self.assertFalse(self.uf.nodes)

    def test_error_if_calling_find_on_node_not_in_uf(self):
        self.assertRaises(KeyError, self.uf.Find, Node())


class singleNodeTest(TestCase):

    def setUp(self):
        self.node = Node()
        self.nodes = set([self.node])
        self.uf = UnionFind(self.nodes)

    def test_node_in_uf(self):
        self.assertIn(self.node, self.uf.nodes)

    def test_find_returns_correct_node(self):
        self.assertEqual(self.node, self.uf.Find(self.node))

    def test_error_if_calling_find_on_node_not_in_uf(self):
        self.assertRaises(KeyError, self.uf.Find, Node())


class twoNodeTest(TestCase):

    def setUp(self):
        self.node1 = Node()
        self.node2 = Node()
        self.nodes = set([self.node1, self.node2])
        self.uf = UnionFind(self.nodes)

    def test_nodes_in_uf(self):
        self.assertIn(self.node1, self.uf.nodes)
        self.assertIn(self.node2, self.uf.nodes)

    def test_find_returns_correct_node(self):
        self.assertEqual(self.node1, self.uf.Find(self.node1))
        self.assertEqual(self.node2, self.uf.Find(self.node2))

    def test_union_changes_nodes_root(self):
        self.uf.Union(self.node1, self.node2)
        self.assertEqual(self.node1, self.node2.root)
        self.assertEqual(self.node1, self.node1.root)

    def test_find_works_after_union(self):
        self.uf.Union(self.node1, self.node2)
        self.assertEqual(self.node1, self.uf.Find(self.node1))
        self.assertEqual(self.node1, self.uf.Find(self.node2))

    def test_error_if_calling_find_on_node_not_in_uf(self):
        self.assertRaises(KeyError, self.uf.Find, Node())


class threeNodeTest(TestCase):

    def setUp(self):
        self.node1 = Node()
        self.node2 = Node()
        self.node3 = Node()
        self.nodes = set([self.node1, self.node2, self.node3])
        self.uf = UnionFind(self.nodes)

    def test_nodes_in_uf(self):
        self.assertIn(self.node1, self.uf.nodes)
        self.assertIn(self.node2, self.uf.nodes)
        self.assertIn(self.node3, self.uf.nodes)

    def test_find_returns_correct_node(self):
        self.assertEqual(self.node1, self.uf.Find(self.node1))
        self.assertEqual(self.node2, self.uf.Find(self.node2))
        self.assertEqual(self.node3, self.uf.Find(self.node3))

    def test_union_changes_nodes_root(self):
        self.uf.Union(self.node1, self.node2)
        self.assertEqual(self.node1, self.node2.root)
        self.assertEqual(self.node1, self.node1.root)
        self.assertEqual(self.node3, self.node3.root)

    def test_find_works_after_union(self):
        self.uf.Union(self.node1, self.node2)
        self.assertEqual(self.node1, self.uf.Find(self.node1))
        self.assertEqual(self.node1, self.uf.Find(self.node2))
        self.assertEqual(self.node3, self.uf.Find(self.node3))

    def test_double_union(self):
        self.uf.Union(self.node1, self.node2)
        self.uf.Union(self.node1, self.node3)
        self.assertEqual(self.node1, self.node2.root)
        self.assertEqual(self.node1, self.node1.root)
        self.assertEqual(self.node1, self.node3.root)

    def test_union_from_node_whos_root_is_not_itself(self):
        self.uf.Union(self.node1, self.node2)
        self.uf.Union(self.node2, self.node3)
        self.assertEqual(self.node1, self.node2.root)
        self.assertEqual(self.node1, self.node1.root)
        self.assertEqual(self.node1, self.node3.root)
 
    def test_error_if_calling_find_on_node_not_in_uf(self):
        self.assertRaises(KeyError, self.uf.Find, Node())


if __name__ == '__main__':
    unittest.main()

