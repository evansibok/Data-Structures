from d_ll import DoublyLinkedList

# {
#     1: 1,
#     2: 2,
#     3: 3
# }


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache. 

        The newly-added pair should be considered the most-recently used entry in the cache.

        If the cache is already at max capacity before this entry is added, then the oldest entry in the cache needs to be removed to make room. 

        Additionally, in the case that the key already exists in the cache, we simply want to overwrite the old value associated with the key with the newly-specified value.
        """
        # Pseudocode from lecture

        # if the key exists in the storage
        if key in self.storage:
            # --> extrapolate the node from the storage at the index of key
            node = self.storage[key]
            # --> set the nodes value to the (key, value) pair
            node.value = (key, value)
            # --> move the node to the end of the order list
            self.order.move_to_end(node)
            # --> just return from the method
            return
        # if the size is equal to the limit
        if self.size == self.limit:
            # --> get the ordered list head
            head = self.order.head
            # --> get the value of the head, which should be a (key, value) pair
            val = head.value
            # --> delete the storage entry at the key from the order lists head's value (which will be the first index)
            del self.storage[val[0]]
            # --> remove the head of the order
            self.order.remove_from_head()
            # --> decrement the size
            self.size -= 1

        # add the (key, value) pair to the tail of the order
        self.order.add_to_tail((key, value))
        # set the storage at the key to the order tail
        self.storage[key] = self.order.tail
        # increment the size
        self.size += 1

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        # Pseudocode from lecture

        # if the key exists in the storage
        if key in self.storage:
            # --> extrapolate the node from the storage at the index of key
            node = self.storage[key]
            # --> move the node to the end of the order list
            self.order.move_to_end(node)
            # --> return the value from the node
            return node.value[1]
        # otherwise
        else:
            # --> return None
            return
