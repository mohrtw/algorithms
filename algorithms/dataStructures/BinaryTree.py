from algorithms.dataStructures.stack import Stack
from algorithms.dataStructures.queue import Queue


from algorithms.utils.exceptions import returnValue


class BinaryTreeNode():

    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def transverse(self, fcn=None, *args, **kwargs):
        q = Queue()
        q.enqueue(self)

        while not q.is_empty():
            curNode = q.dequeue()

            if curNode.left:
                q.enqueue(curNode.left)

            if fcn:
                try:
                    fcn(curNode, *args, **kwargs)
                except returnValue as v:
                    return v.value

            if curNode.right:
                q.enqueue(curNode.right)

    def transverse_inorder(self, fcn=None, *args, **kwargs):
        s = Stack()
        s.push(self)

        while not s.is_empty():
            # if the top of the stack is a node, attempt to add its
            # children to the stack,
            # otherwise, call fcn on the top item of the stack
            if isinstance(s.peek(), BinaryTreeNode):
                curNode = s.pop()

                if curNode.right:
                    s.push(curNode.right)

                if fcn:
                    s.push((curNode,))

                if curNode.left:
                    s.push(curNode.left)

            else:
                curNode, = s.pop()
                try:
                    fcn(curNode, *args, **kwargs)
                except returnValue as v:
                    return v.value

    def transverse_preorder(self, fcn=None, *args, **kwargs):
        if fcn:
            fcn(self.value, *args, **kwargs)
        if self.left:
            self.left.transverse_preorder(fcn, *args, **kwargs)
        if self.right:
            self.right.transverse_preorder(fcn, *args, **kwargs)

    def transverse_postorder(self, fcn=None, *args, **kwargs):
        if self.left:
            self.left.transverse_postorder(fcn, *args, **kwargs)
        if self.right:
            self.right.transverse_postorder(fcn, *args, **kwargs)

        if fcn:
            fcn(self.value, *args, **kwargs)


class BinaryTree():

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def contains(self, value):

        def raiseReturnTrueIfMatches(node, compValue):
            if node.value == compValue:
                raise returnValue(True)

        if self.root.transverse(raiseReturnTrueIfMatches, value):
            return True

        return False

    def insert(self, value):
        """transverses the binary tree and inserts value at first empty node"""
        def returnFirstNodeWithEmptyChild(node):
            if node.left is None or node.right is None:
                raise returnValue(node)

        if self.root:
            node = self.root.transverse(returnFirstNodeWithEmptyChild)

            if node.left is None:
                node.left = BinaryTreeNode(value)
            elif node.right is None:
                node.right = BinaryTreeNode(value)

        else:
            self.root = BinaryTreeNode(value)
