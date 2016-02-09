# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        len_a = self.getLength(A)
        len_b = self.getLength(B)
        current_a = A
        current_b = B

        if len_a > len_b:
            diff = len_a - len_b

            for _ in range(diff):
                current_a = current_a.next

        elif len_b > len_a:
            diff = len_b - len_a

            for _ in range(diff - 1):
                current_b = current_b.next

        print current_a.val, current_b.val
        while current_a != current_b:
            current_a = current_a.next
            current_b = current_b.next

        return current_a

    def getLength(self, A):
        list_length = 1

        while A.next != None:
            A = A.next
            list_length += 1

        return list_length


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

d = ListNode(4)
d.next = c

result = Solution()

result = result.getIntersectionNode(a, d)

print result.val
