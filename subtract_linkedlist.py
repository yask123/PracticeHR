class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):

        current = A
        length = self.calc_len(A)

        for i in range(length // 2):
            current.val = self.kth_node_from_last(A, i, length) - current.val
            current = current.next
        return A

    def calc_len(self, A):
        list_length = 1

        while (A.next != None):
            list_length += 1
            A = A.next

        return list_length

    def kth_node_from_last(self, A, k, l):
        how_far_to_go = l - k
        current_node = A

        for _ in range(how_far_to_go - 1):
            current_node = current_node.next

        return current_node.val


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

result = Solution()
head = result.subtract(a)

while (head != None):
    print head.val
    head = head.next
