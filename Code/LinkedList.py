class LinkedList():
    #TODO https://www.programiz.com/python-programming/property
    class Node():
        def __init__(self, value = None, next = None):
            self.value = value
            self.setNext(next)

        def __repr__(self):
            return str(self.value)

        def setNext(self, next):
            self.next = None
            if isinstance(next, type(self)):
                self.next = next
            return self.next

        def getNext(self):
            return self.next

        def getValue(self):
            return self.value

    def __init__(self, head = None):
        self.length = 0
        self.head = None
        self.tail = None
        if isinstance(head, self.Node):
            self.head = head
            self.tail = head
        #self.beforeTail = None

    def __len__(self):
        return self.length

    def __repr__(self):
        listOfNodes = [ str(value) for value in self]
        if not listOfNodes:
            return str(None)
        return " -> ".join( listOfNodes )

    def __bool__(self):
        return self.length > 0

    def __add__(self, other):
        pass

    def __iter__(self):
        self.currentNode = self.head
        return self

    def __next__(self):
        node = self.currentNode
        if node:
            self.currentNode = self.currentNode.getNext()
            return node.value
        else:
            raise StopIteration

    def getNode(self, position):
        if position < 0 or position >= self.length:
            return None

        currentNode = self.head
        for _ in range(position):
            currentNode = currentNode.getNext()

        return currentNode

    def splitAt(self, splitIndex):
        pass

    def insert(self, value, position):
        if position < 0 or position > self.length:
            return None
            #raise

        newNode = self.Node(value)
        previousNode = None
        currentNode = self.head
        for _ in range(position):
            previousNode = currentNode
            currentNode = currentNode.getNext()

        newNode.setNext(currentNode)
        if previousNode:
            previousNode.setNext(newNode)
        else:
            self.head = newNode
        self.length += 1

        return newNode

    def push(self, value):
        return self.insert(value, 0)

    def pop(self, position = 0, default = None):
        if position < 0 or position >= self.length:
            return None

        previousNode = None
        currentNode = self.head
        for _ in range(position):
            previousNode = currentNode
            currentNode = currentNode.getNext()

        if not currentNode:
            return default
        if previousNode:
            previousNode.setNext(currentNode.getNext())
        else:
            self.head = currentNode.getNext()
        self.length -= 1

        nodeValue = currentNode.value
        del currentNode
        return nodeValue

    def append(self, value):
        pass



class DoubleLinkedList(LinkedList):
    class Node(LinkedList.Node):
        def __init__(self, value = None, previous = None, next = None):
            super().__init__(value, next)
            self.setPrevious(previous)

        def setPrevious(self, previous):
            self.previous = None
            if isinstance(previous, type(self)):
                self.previous = previous
            return self.previous

        def getPrevious(self):
            return self.previous

    def __init__(self):
        super().__init__()
        #del self.beforeTail

    #TODO
    def insert(self, value, position):
        if position < 0 or position > self.length:
            return None

        newNode = self.Node(value)
        #TODO optimization for going the other way
        #closestPosition, direction, startingNode = min( (position, getNext, self.head), (self.length - position, getPrevious, self.tail) )
        currentNode = self.head
        for _ in range(position):
            currentNode = currentNode.getNext()

        extremePosition = False
        if position == 0:
            newNode.setNext(self.head)
            if self.head:
                self.head.setPrevious(newNode)
            self.head = newNode
            extremePosition = True
        if position == self.length:
            newNode.setPrevious(self.tail)
            if self.tail:
                self.tail.setNext(newNode)
            self.tail = newNode
            extremePosition = True
        if not extremePosition:
            previousNode = currentNode.getPrevious()

            newNode.setNext(currentNode)
            currentNode.setPrevious(newNode)

            newNode.setPrevious(previousNode)
            previousNode.setNext(newNode)


        self.length += 1

        return newNode

    def pop(self, position = 0, default = None):
        if position < 0 or position >= self.length:
            return None


        closestPosition, direction, startingNode = (position, self.Node.getNext, self.head)
        if self.length - position -1 < closestPosition:
            closestPosition, direction, startingNode = (self.length - position -1, self.Node.getPrevious, self.tail)
        currentNode = startingNode
        for _ in range(closestPosition):
            currentNode = direction(currentNode)

        if not currentNode:
            return default
        previousNode = currentNode.getPrevious()
        nextNode = currentNode.getNext()
        if position == 0:
            self.head = nextNode
        if position == self.length-1:
            self.tail = previousNode
        if nextNode:
            nextNode.setPrevious(previousNode)
        if previousNode:
            previousNode.setNext(nextNode)

        self.length -= 1

        nodeValue = currentNode.value
        del currentNode
        return nodeValue


if __name__ == "__main__":
    array = []
    ll = DoubleLinkedList()
    ll.push(3)
    print(ll)
    ll.push(2)
    print(ll)
    ll.push(1)
    print(ll)
    ll.insert(5, 3)
    ll.insert(4, 3)
    print(ll)
    for i in range(len(ll)):
        print(i, ll.pop())
