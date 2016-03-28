class Stack(object):
    """Represents a last-in, first-out data structure

    Public attributes:
    - items: A list of items in the stack.

    Functions:
    - push: Pushes an item to the end of the stack.
    - pop: Removes and returns the last item in the stack.
    - peek: Returns the last item in the stack.
    - is_empty: Returns True if the stack contains no elements.
    """

    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, item):
        """Pushes an item to the end of the stack.

        Args:
            item: the item to be pushed to the stack.
        """
        self.items.append(item)

    def pop(self):
        """Removes and returns the last item in the stack.

        Returns:
            The last item in the stack.
        """
        return self.items.pop()

    def peek(self):
        """Returns the last item in the stack.
        """
        return self.items[-1]

    def is_empty(self):
        """Returns True if the stack is empty.
        """
        return not self.items
