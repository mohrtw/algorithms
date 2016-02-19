from .DoublyLinkedList import DoublyLinkedList


class Queue():
    def __init__(self):
        self.items = DoublyLinkedList()

    def enqueue(self, data):
        self.items.insert_end(data)

    def dequeue(self):
        n = self.items.get_head()
        self.items.delete(0)
        return n.data

    def peek(self):
        return self.items.get_head().data
