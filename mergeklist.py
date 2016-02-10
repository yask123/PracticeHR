# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        my_heap = []
        for each_list_node in A:
            current = each_list_node
            while current != None:
                heapq.heappush(my_heap, current.val)
                current = current.next
        result = []
        prev = heapq.heappop(ListNode(my_heap))
        new_head = prev
        while len(my_heap) > 0:
            new_node = ListNode(heapq.heappop(ListNode(my_heap)))
            prev.next = new_node
            prev = new_node

        return new_head


a = Solution()
print a.mergeKLists([[1, 2, 11], [5, 6, 7]])
