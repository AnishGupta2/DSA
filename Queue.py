class CirQueue:
    def __init__(self,maxsize):
        self.items = maxsize*[None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(i) for i in self.items]
        return '\n'.join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.top + 1 == self.maxsize and self.start == 0:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self,value):
        if self.top + 1 == self.maxsize:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
  
#Queue using Linked List  
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
        
class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def __str__(self):
        value = [str(i) for i in self.items]