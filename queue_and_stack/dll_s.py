from d_ll import DoublyLinkedList


# Last In First Out
# Push (Add to stack)
# Pop (Remove from stack)
class Stack:
    """
    The stack data structure implemented with methods to push, pop and return the size of the stack. Utilizing Last In First Out (LIFO).
    """

    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def push(self, value):
        """
        Adds an item to the stack using the DLL as storage.
        """
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        """
        Removes an item to the stack using the DLL as storage.
        """
        # Check if stack is empty
        if self.size == 0:
            # If it is, return Nothing
            return
        # otherwise
        else:
            # decrement the stack
            self.size -= 1
            # remove the last added item from the tail
            return self.storage.remove_from_head()

    def len(self):
        """
        Returns the size of the stack
        """
        return self.size


s = Stack()
