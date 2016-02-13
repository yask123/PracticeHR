'''
https://www.interviewcake.com/question/python/balanced-binary-tree
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root, depth):
    if root == None:
        return True

    left_tree_depth = isBalanced(root.left, depth + 1)
    right_tree_depth = isBalanced(root.righ, depth + 1)

    if abs(left_tree_depth - right_tree_depth) > 1:
        return False

    return max(left_tree_depth, right_tree_depth)
