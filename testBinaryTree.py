'''
https://www.interviewbit.com/courses/programming/topics/trees/problems/validbst/
'''


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


import sys

MAX_INT = sys.maxint
MIN_INT = -sys.maxint - 1


def isBST(root):
    stack = [(root, MAX_INT, MIN_INT)]

    # Depth search
    while len(stack) > 0:
        node, lower_bound, upper_bound = stack.pop()

        if node.value < lower_bound or node.value > upper_bound:
            return False

        if node.left:
            # This node must be less than current node
            stack.append((node.left, lower_bound, node.value))

        if node.right:
            # This node must be greater than current node
            stack.append((node.right, node.value, upper_bound))

        return True
