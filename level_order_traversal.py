class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def levelOrder(self, A):
        current_level = deque([A])
        next_level = deque()
        levels = [[A.val]]
        while current_level:
            node = current_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not current_level:
                if next_level:
                    levels.append([n.val for n in next_level])
                current_level = next_level
                next_level = deque()
        return levels
