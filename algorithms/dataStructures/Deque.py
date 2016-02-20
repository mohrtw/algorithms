from .DoublyLinkedList import DoublyLinkedList


class Deque():

    def __init__(self):
        self.items = DoublyLinkedList()

    def inject(self, data):
        self.items.insert_start(data)

    def push(self, data):
        self.items.insert_end(data)

    def eject(self):
        n = self.items.get_tail()
        self.items.delete_tail()
        return n.data

    def pop(self):
        n = self.items.get_head()
        self.items.delete_head()
        return n.data

    def peek_last(self):
        return self.items.get_tail().data

    def peek_first(self):
        return self.items.get_head().data
