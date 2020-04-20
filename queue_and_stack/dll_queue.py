# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class NodeList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def isEmpty(self):
        return self.storage.head is None

    # def peek(self):
    #     if self.storage.head is None:
    #         return self.storage.head
    #     else:
    #         return self.storage.head

    def enqueue(self, value):
        self.size += 1
        new_node = NodeList(value, None)
        if self.storage.tail is not None:
            self.storage.tail = new_node
        # pass

    def dequeue(self):
        pass

    def len(self):
        pass


qb = Queue()


print(qb.isEmpty())
