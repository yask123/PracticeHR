# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys


class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        return self.calc(A, 0)

    def calc(self, A, depth):
        # print A.val,depth
        if A.left == None and A.right == None:
            return depth
        left_tree_height = sys.maxint
        right_tree_height = sys.maxint
        if A.left != None:
            left_tree_height = self.calc(A.left, depth + 1)
        if A.right != None:
            right_tree_height = self.calc(A.right, depth + 1)
        # print A.val,left_tree_height,right_tree_height
        return min(left_tree_height, right_tree_height)


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)

b.right = c
b.left = a
c.right = d

sol = Solution()
print sol.calc(b, 0)
