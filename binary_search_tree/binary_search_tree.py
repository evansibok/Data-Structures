import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Create a new node
        new_node = BinarySearchTree(value)

        # Starting at the root,
        # Check if there is a root, if not, the root becomes the new node
        if self.value is None:
            self.value = new_node.value
            return self.value

        # If there is a root, check if the value of the new node is greater than or less than the value of the root
        # If it is greater,
        if value >= self.value:
            # -> Check to see if there is a node to the right
            if self.right is not None:
                # -> If there is, then move to that node and repeat these steps
                self.right.insert(value)
        # If there is not, add that node as the right property
            else:
                self.right = new_node

        # If it is less,
        else:
            # check to see if there is a node to the left
            # -> If there is then move to that node and repeat these steps
            if self.left is not None:
                self.left.insert(value)
        # If there is not, add that node as the left property
            else:
                self.left = new_node

    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
