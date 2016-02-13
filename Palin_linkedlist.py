# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def nth_node(self, A, n):
        for _ in range(n):
            A = A.next
        return A

    def get_length(self, A):
        l = 1
        current = A

        while current.next != None:
            current = current.next
            l += 1
        return l

    def lPalin(self, A):
        nodes_length = self.get_length(A)

        for i in range(nodes_length // 2):
            j = nodes_length - i
            if self.nth_node(A, i).val != self.nth_node(A, j - 1).val:
                return 0

        return 1


A = ListNode(1)
B = ListNode(2)
C = ListNode(0)
A.next = B
B.next = C

a = Solution()

print a.lPalin(A)
