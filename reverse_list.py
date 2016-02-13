# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        current = A
        prev = None
        if current.next != None:
            # Atleast 2 nodes
            prev = A
            current = prev.next

        while current.next != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        current.next = prev
        A.next = None
        return current
