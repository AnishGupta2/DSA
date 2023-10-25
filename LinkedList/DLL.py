class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    #
    def createDLL(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
    
    #
    def insert(self,value,index):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newnode = Node(value)
            if index == 0:
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            elif index == -1:
                self.tail.next = newnode
                newnode.prev = self.tail
                self.tail = newnode
            else:
                temp =  self.head
                for i in range(index-1):
                    temp = temp.next
                newnode.prev = temp
                newnode.next = temp.next
                temp.next.prev = newnode
                temp.next = newnode
    
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    #  Reverse Traversal Method in Doubly Linked List
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search Method in Doubly Linked List
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"
    def delete(self,index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == -1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            tempnext = temp.next
            temp.next = tempnext.next 
            tempnext.prev = temp
        
                
    
