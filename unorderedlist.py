class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        length = 0
        while current != None:
            length += 1
            current = current.next
        return length

    def search(self, value):
        current = self.head
        index = -1
        while (current != None):
            index += 1
            if current.data == value:
                return index
            current = current.getNext()
        return -1

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while (current != None):

            if current.data == item:
                found = True
                break
            previous = current
            current = current.getNext()

        if found:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.next = current.next


l = UnorderedList()
l.add(2)
l.add(3)
l.add(4)
l.remove(2)
print l.search(3)
