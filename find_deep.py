# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def calc(self, A, l):
        left_len = 0
        right_len = 0
        if A.left != None:
            self.calc(A.left, l + 1)
        if A.right != None:
            self.calc(A.right, l + 1)
        print left_len, right_len
        return max(left_len, right_len)

    def maxDepth(self, A):
        return self.calc(A, 0)


s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.right = c
print s.maxDepth(a)
