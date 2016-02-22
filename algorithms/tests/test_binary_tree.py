import unittest
from unittest import TestCase

from algorithms.dataStructures.BinaryTree import BinaryTreeNode
from algorithms.dataStructures.BinaryTree import BinaryTree


class binary_tree_creation_Test(TestCase):

    def test_create_node(self):
        n = BinaryTreeNode(1)
        self.assertIsInstance(n, BinaryTreeNode)

    def test_create_node_assigns_correct_data(self):
        n = BinaryTreeNode(1)
        self.assertEqual(1, n.value)

    def test_create_node_assigns_None_to_left_right_parent(self):
        n = BinaryTreeNode(1)
        self.assertIsNone(n.left)
        self.assertIsNone(n.right)
        self.assertIsNone(n.parent)

    def test_create_binary_tree(self):
        bt = BinaryTree()
        self.assertIsInstance(bt, BinaryTree)

    def test_create_binary_tree_with_one_node(self):
        n = BinaryTreeNode(1)
        bt = BinaryTree(n)
        self.assertEqual(n, bt.root)
        self.assertEqual(1, bt.root.value)
        self.assertIsNone(bt.root.parent)

    def test_create_linked_list_with_multiple_nodes(self):
        nr = BinaryTreeNode(3)
        nl = BinaryTreeNode(2)
        n = BinaryTreeNode(1, nl, nr)

        bt = BinaryTree(n)
        self.assertEqual(n, bt.root)
        self.assertEqual(1, bt.root.value)

        self.assertEqual(nl, bt.root.left)
        self.assertEqual(2, bt.root.left.value)

        self.assertEqual(nr, bt.root.right)
        self.assertEqual(3, bt.root.right.value)


class empty_Test(TestCase):

    def test_empty_Tree(self):
        bt = BinaryTree()
        self.assertTrue(bt.is_empty())

    def test_one_element_Tree(self):
        bt = BinaryTree(BinaryTreeNode(1))
        self.assertFalse(bt.is_empty())


class transversal_Test(TestCase):

    def setUp(self):
        nrr = BinaryTreeNode(7)
        nrl = BinaryTreeNode(6)
        nlr = BinaryTreeNode(5)
        nll = BinaryTreeNode(4)
        nr = BinaryTreeNode(3, nrl, nrr)
        nl = BinaryTreeNode(2, nll, nlr)
        n = BinaryTreeNode(1, nl, nr)

        self.bt = BinaryTree(n)

    def test_level_order(self):
        output = ''

        def fcn(node):
            nonlocal output
            output += str(node.value) + ' '

        self.bt.root.transverse(fcn)

        self.assertEqual("1 2 3 4 5 6 7 ", output)

    def test_inorder(self):
        output = ''

        def fcn(node):
            nonlocal output
            output += str(node.value) + ' '

        self.bt.root.transverse_inorder(fcn)

        self.assertEqual("4 2 5 1 6 3 7 ", output)

    def test_preorder(self):
        output = ''

        def fcn(value):
            nonlocal output
            output += str(value) + ' '

        self.bt.root.transverse_preorder(fcn)

        self.assertEqual("1 2 4 5 3 6 7 ", output)

    def test_postorder(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.bt.root.transverse_postorder(print)
            output = out.getvalue().strip()
            self.assertEqual(output, "4\n5\n2\n6\n7\n3\n1")
        finally:
            sys.stdout = saved_stdout


class contains_Test(TestCase):

    def setUp(self):
        nrr = BinaryTreeNode(7)
        nrl = BinaryTreeNode(6)
        nlr = BinaryTreeNode(5)
        nll = BinaryTreeNode(4)
        nr = BinaryTreeNode(3, nrl, nrr)
        nl = BinaryTreeNode(2, nll, nlr)
        n = BinaryTreeNode(1, nl, nr)

        self.bt = BinaryTree(n)

    def test_contains(self):
        self.assertTrue(self.bt.contains(1))
        self.assertTrue(self.bt.contains(2))
        self.assertTrue(self.bt.contains(3))
        self.assertTrue(self.bt.contains(4))
        self.assertTrue(self.bt.contains(5))
        self.assertTrue(self.bt.contains(6))
        self.assertTrue(self.bt.contains(7))

    def test_does_not_contain(self):
        self.assertFalse(self.bt.contains(8))
        self.assertFalse(self.bt.contains(0))
        self.assertFalse(self.bt.contains('a'))
        self.assertFalse(self.bt.contains(45))
        self.assertFalse(self.bt.contains((1, 2)))
        self.assertFalse(self.bt.contains("tree"))


class insert_Test(TestCase):

    def test_insert_empty_tree(self):
        bt.insert(1)
        assertEqual(1, bt.root.value)

    def test_insert_just_root_node(self):
        n = BinaryTreeNode(1)
        bt = BinaryTree(n)

        bt.insert(2)
        self.assertEqual(2, bt.root.left.value)

    def test_insert_root_and_left_node(self):
        nl = BinaryTreeNode(2)
        n = BinaryTreeNode(1, nl)
        bt = BinaryTree(n)

        bt.insert(3)
        self.assertEqual(3, bt.root.right.value)

    def test_insert_root_and_right_node(self):
        nr = BinaryTreeNode(2)
        n = BinaryTreeNode(1, None, nr)
        bt = BinaryTree(n)

        bt.insert(3)
        self.assertEqual(3, bt.root.left.value)



if __name__ == '__main__':
    unittest.main()
