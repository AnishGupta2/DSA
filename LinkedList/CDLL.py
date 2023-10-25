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
        newnode.next = newnode
        newnode.prev = newnode
    
    def insert(self,value,index):
        newnode = Node(value)
        if index == 0:
            self.head.prev = newnode
            self.tail.next = newnode
            newnode.next = self.head
            newnode.prev =  self.tail
            self.head = newnode
        elif index == -1:
            self.head.prev = newnode
            self.tail.next = newnode
            newnode.next = self.head
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
     # Traversal of Circular Doubly Linked List
    def traversalCDLL(self):
        if self.head is None:
            print("There is not any node for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                tempNode = tempNode.next

    # Reverse traversal of Circular Doubly Linked List
    def reverseTraversalCDLL(self):
        if self.head is None:
            print("There is not any node for reverse traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
    
    # Search Circular Doubly Linked List
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return "There is not any node in CDLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The value does not exist in CDLL"
                tempNode = tempNode.next
            
    def delete(self,index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif index == -1:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail 
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            tempnext = temp.next
            temp.next = tempnext.next 
            tempnext.prev = temp
            