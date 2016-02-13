class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def isCycle(head):
    rabbit = head.next
    tortise = head

    while rabbit != None and tortise != None:
        if rabbit.val == tortise.val:
            return True
        try:
            tortise = tortise.next
            rabbit = rabbit.next.next
        except:
            break
    return False


a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)
d = LinkedListNode(4)

a.next = b
b.next = c
c.next = d
d.next = a

print isCycle(a)
