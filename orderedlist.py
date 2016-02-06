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


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        prev = None
        current = self.head

        while current != None:
            if current.data >= item:
                break
            else:
                prev = current
                current = current.getNext()

        if prev == None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            prev.next = temp

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

    def printall(self):
        current = self.head

        while (current != None):
            print current.data, ' -> ',
            current = current.getNext()


l = OrderedList()
l.add(5)
l.add(3)
l.add(1)
l.add(2)
l.printall()
