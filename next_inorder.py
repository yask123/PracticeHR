'''
https://www.interviewbit.com/courses/programming/topics/trees/problems/inordernext/
               100
              /   \
            98    102
           /  \
         96    99
          \
           97
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def next_inorder_value(root, value):
    # Search the value

    current = root

    while current.val != value:  # O(h)

        if value > current.val:
            current = current.right
        if value < current.val:
            current = current.left

    if current.right != None:
        return find_min(current.right)  # O(h)

    else:
        ancestor = root
        successor = None
        while ancestor != current:
            if ancestor.val > current:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.left
        return successor.val


def find_min(root):
    while root.left != None:
        root = root.left
