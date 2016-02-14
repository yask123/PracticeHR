# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        self.calc(A, 0)

    def calc(self, A, d):
        if A == None:
            return d - 1
        return min(self.calc(A, d + 1), self.calc(A, d + 1))
