# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):

        current_node = A
        next_node = current_node.next
        next_node_next = next_node.next

        while current_node and next_node:

            temp = next_node.next

            next_node.next = current_node
            current_node.next = next_node.next

            current_node = temp
            next_node = current_node.next
            if current_node == None or next_node == None:
                break
            next_node_next = next_node.next
        return current_node
