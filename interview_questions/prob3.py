"""
Reverse a singly linked list without recursion? 
- You may not store the list, or it's values, in another data structure.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"value: {self.value}, next: {self.next}"

    def add(self, value):
        self.next = Node(value)


class LinkedList:
    pass

    def reverse_list(self, node, prev):

        pass
