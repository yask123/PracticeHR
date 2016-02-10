# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def findMin(self, A):
        current = A
        while current.left != None:
            current = current.left
        return current

    def getSuccessor(self, A, B):

        current = A

        while current != None:
            if current.val == B:
                if current.right != None:
                    # It has a right subtree
                    return self.findMin(current.right)
                else:
                    ancestor = A
                    successor = None

                    while ancestor != current:
                        if current.val < ancestor.val:
                            successor = ancestor
                            ancestor = ancestor.left
                        else:
                            ancestor = ancestor.right
                    return successor

            elif B > current.val:
                current = current.right
            else:
                current = current.left
