# Definition for a  binary tree node
# https://www.interviewbit.com/courses/programming/topics/trees/problems/invert/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        self.invert_tree(root)
        return root

    def invert_tree(self, A):
        if A != None:
            left_sub_tree = A.left
            right_sub_tree = A.right

            A.left = right_sub_tree
            A.right = left_sub_tree

            self.invert_tree(A.left)
            self.invert_tree(A.right)
