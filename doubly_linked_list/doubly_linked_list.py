"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        self.length += 1
        # instantiate a new node setting prev and next to None
        new_node = ListNode(value, None, None)
        # Check if head and tail already exists (there is at least 1 item in the list)
        # if no head and tail exists already
        if not self.head and not self.tail:
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # assign the current head to a temp
            temp = self.head
            # set the prev of the current head to the new node
            self.head.prev = new_node
            # make a new current head with the new node
            self.head = new_node
            # set the next of the current head to the temp
            self.head.next = temp

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        self.length -= 1
        # if no current head return False
        # if current head exists
        # set the current head to a temp
        #
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        self.length += 1

        new_node = ListNode(value, None, None)

        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            # set the current tail to a temp
            temp = self.tail
            # point the current tail's next to the new node
            self.tail.next = new_node
            # set the current tail to the new node
            self.tail = new_node
            # set the current tail's prev to the temp (old tail)
            self.tail.prev = temp

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        pass

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass
