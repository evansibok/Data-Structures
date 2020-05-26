from d_ll import DoublyLinkedList


# First In First Out
# Enqueue (Add to queue)
# Dequeue (Remove from queue)
class Queue:
    """
    The queue data structure implemented with methods to enqueue, dequeue and return the size of the queue. Utilizing First In First Out (FIFO).
    """

    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """
        Adds an item to the front (tail) of the queue.
        """
        # Increase the size of the queue
        self.size += 1
        # Using a dll as storage
        # Add a node to the tail
        return self.storage.add_to_tail(value)

    def dequeue(self):
        """
        Removes an item from the front (tail) of the queue.
        """
        # Check if queue is empty
        if self.size == 0:
            # If it is, do nothing
            return
        # otherwise
        else:
            # Using the same dll as storage
            # Decrement the size of the queue
            self.size -= 1
            # Remove a node from the tail
            return self.storage.remove_from_head()

    def len(self):
        """
        Returns the size of the queue
        """
        return self.size
