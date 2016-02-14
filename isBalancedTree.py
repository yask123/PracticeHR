# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def calc(self, root, lower_bound, upper_bound):
        # print root.val,lower_bound,upper_bound,'initial'
        if root.val <= lower_bound or root.val >= upper_bound:
            # print root.val,lower_bound,upper_bound,'fail'
            return 0
        left_tree_balanced = 1
        right_tree_balanced = 1
        if root.left != None:
            left_tree_balanced = self.calc(root.left, lower_bound, root.val)
        if root.right != None:
            right_tree_balanced = self.calc(root.right, root.val, upper_bound)
        # print root.val,left_tree_balanced,right_tree_balanced
        if left_tree_balanced == 1 and right_tree_balanced == 1:
            return 1
        else:
            return 0

    def isValidBST(self, A):
        return self.calc(A, float('-inf'), float('inf'))


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(3)
e = TreeNode(4)

c.left = b
c.right = e
b.left = a
b.right = d

sol = Solution()
print sol.isValidBST(c), 'ans'
