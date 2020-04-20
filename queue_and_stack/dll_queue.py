# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # self.head = node
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def peek(self):
        if self.storage.head is None:
            return "Queue is empty!"
        else:
            return self.storage.head

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def len(self):
        pass


qb = Queue()


print(qb.peek())
