# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def nodelength(self, A):
        l = 1
        while A != None:
            A = A.next
            l += 1
        return l

    def addTwoNumbers(self, A, B):
        carry = 0
        first = None
        prev = None
        a_node_length = self.nodelength(A)
        b_node_length = self.nodelength(B)
        if a_node_length > b_node_length:
            diff = a_node_length - b_node_length
            for _ in range(a_node_length):
                cu
            for _ in range(diff):

        while A != None and B != None:
            value = A.val + B.val + carry
            value = str(value)
            carry, current_value = value[:-1], int(value[-1])
            if carry != '':
                carry = int(carry)
            else:
                carry = 0
            current_node = ListNode(current_value)
            if first == None:
                first = current_node
            if prev != None:
                prev.next = current_node
            prev = current_node
            A = A.next
            B = B.next

        return first


a = ListNode(1)
b = ListNode(1)
a.next = b

c = ListNode(1)

s = Solution()
test = s.addTwoNumbers(a, c)

while test != None:
    print test.val,
    test = test.next
