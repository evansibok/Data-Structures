"""
Single Linked List implementation with a method that counts existing number of nodes
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # New node to add to list
        new_node = ListNode(value)

        # If head does not exist
        # Point the head to the new node item
        # Point the tail to the new node item
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:  # [b, c, d] -> current list
            # [a] -> item on new_node to add
            # Add the item on new_node to a temporary variable to hold
            temp = new_node
            # Set the item next of the new_node to the current item on the head
            new_node.next = self.head
            # Set the head to the new_node item saved to the temporary variable
            self.head = temp

    def count_node(self):
        count = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count


lil = LinkedList()

print(lil.add_to_head(4))
print(lil.count_node())
print(lil.add_to_head(2))
print(lil.count_node())
print(lil.add_to_head(1))
print(lil.count_node())
