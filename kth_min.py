# Definition for a  binary tree node
'''
For example,
		 1
		/ \
	  2    3
		  /
		4
		 \
		  5
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @param k : integer
    # @return an integer
    ans = 0
    flag = 0

    def helper(self, root, k):

        if root.left:
            self.helper(root.left, k)

        if self.flag == 0:
            self.ans = root.val
        self.flag -= 1

        if root.right:
            self.helper(root.right, k)

    def kthsmallest(self, root, k):
        self.flag = k - 1
        self.helper(root, k - 1)
        return self.ans


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(0)

b.right = c
b.left = a
a.left = d

r = Solution()
print r.kthsmallest(b, 2)
