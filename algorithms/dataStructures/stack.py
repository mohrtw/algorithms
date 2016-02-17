class Stack(object):

    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
