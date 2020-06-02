"""
Given a sorted array of distinct non-negative integers,
find the smallest missing element in it.
"""

# Examples

# _Input: _ `A = [0, 1, 2, 6, 9, 11, 15]`
# _Output: _ The smallest missing element is 3

# _Input: _ `A = [1, 2, 3, 4, 6, 9, 11, 15]`
# _Output: _ The smallest missing element is 0

# _Input: _ `A = [0, 1, 2, 3, 4, 5, 6]`
# _Output: _ The smallest missing element is 7


# recursive solution (linked list)
def smallest_missing(arr, left, right):
    # Edge Case
    # if arr is empty return None
    if not arr:
        return None

    # Base Case

    # loop through the array
    # record the position(index) of the current element
    # while the current index matches the value of the current element
        # record the values to the left and to the right of the current element
        # if the the position(index) of the current element does not
        # match the value in that index
        # set that value as the smallest missing element
    # and return the value


if __name__ == '__main__':
    A = [0, 1, 2, 6, 9, 11, 15]
    print(
        f"The smallest missing element is {smallest_missing(A, 0, len(A) - 1)}")

    A = [1, 2, 3, 4, 6, 9, 11, 15]
    print(
        f"The smallest missing element is {smallest_missing(A, 0, len(A) - 1)}")

    A = [0, 1, 2, 3, 4, 5, 6]
    print(
        f"The smallest missing element is {smallest_missing(A, 0, len(A) - 1)}")
