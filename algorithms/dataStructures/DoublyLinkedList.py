class DoublyLinkedNode():

    def __init__(self, data, next_=None, previous_=None):
        self.data = data
        self.next = next_
        self.previous = previous_

        if self.next:
            self.next.previous = self

        if self.previous:
            self.previous.next = self


class DoublyLinkedList():

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

        if self.head is not None and self.tail is None:
            self.tail = self.head

        # transverse node until the tail is found
        if self.tail:
            while self.tail.next:
                self.tail = self.tail.next

    def get_element(self, position):

        if self.head is None:
            return None

        elif position == 0:
            return self.head

        # transverse linked list until the position is reached
        else:
            curNode = self.head
            pos = 1

            while pos <= position:
                curNode = curNode.next
                pos += 1

            return curNode

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def insert_end(self, data):
        n = DoublyLinkedNode(data, next_=None, previous_=self.tail)

        if self.head is None:
            self.head = n
            self.tail = n

        elif self.head is self.tail:
            self.tail = n
            self.head.next = n
            self.tail.previous = self.head

        else:
            self.tail.next = n
            self.tail = n

    def insert_start(self, data):
        n = DoublyLinkedNode(data, self.head)

        if self.head is None:
            self.head = n
            self.tail = n

        elif self.head is self.tail:
            self.tail = self.head
            self.head = n
            self.tail.previous = self.head

        else:
            self.head = n

    def insert(self, data, position):

        n = DoublyLinkedNode(data)

        if self.head is None:
            self.head = n
            self.tail = n

        elif position == 0:
            n.next = self.head
            self.head = n

        # transverse linked list until the position is reached
        else:
            curNode = self.head
            pos = 1

            while pos < position:
                curNode = curNode.next
                pos += 1

            n.next = curNode.next
            if n.next:
                n.next.previous = n
            curNode.next = n
            n.previous = curNode

            if curNode is self.tail:
                self.tail = n

    def delete(self, position):

        if position == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None

            elif self.head.next == self.tail:
                self.head = self.tail
                self.tail.previous = None

            else:
                self.head = self.head.next
                self.head.previous = None

        else:
            curNode = self.head
            pos = 1
            while pos < position:
                curNode = curNode.next
                pos += 1

            if curNode.next is self.tail:
                self.tail = curNode

            curNode.next = curNode.next.next
            if curNode.next:
                curNode.next.previous = curNode

    def display(self):
        curNode = self.head
        while curNode:
            print(curNode.data)
            curNode = curNode.next
