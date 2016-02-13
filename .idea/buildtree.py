# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

Return :
            1
           / \
          2   3

'''

class Solution:
    # @param preorder : list of integers denoting preorder traversal of tree
    # @param inorder : list of integers denoting inorder traversal of tree
    # @return the root node in the tree
    def buildTree(self, preorder, inorder):
        root_value = preorder[0]
        root_index = inorder.index(root_value)

        left_nodes = inorder[:root_index]
        right_nodes = inorder[root_index+1:]

        m = len(left_nodes)
        n = len(right_nodes)

        root = TreeNode(root_value)
        root.left = self.buildTree(preorder[:m+1],left_nodes)
        root.right = self.buildTree(preorder[m+1:],right_nodes)

        return root

