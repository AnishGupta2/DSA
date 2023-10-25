class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1
        
    def prepend(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            self.length +=1
            
    def insert(self,value,index):
        newnode = Node(value)
        if index <0 or index > self.length:
            return False
        elif self.head == None:
            self.head = newnode
            self.tail = newnode
        elif index == 0:
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            for i in range(0,index-1):
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode
        if newnode.next == None:
            self.tail = newnode
        self.length +=1
        
    def get(self,index):
        if index <0 or index > self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.value
    
    def set(self,index,value):
        if index <0 or index > self.length:
            return False
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = value
        return True
    
    def popfirst(self):
        popped = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped.next = None
        self.length -=1
        return popped
    
    def pop(self):
        popped = self.tail
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        return popped

    def remove(self,index):
        if self.length ==1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.popfirst()     
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            removed = temp.next
            temp.next = removed.next
            removed.next = None
    def deleteall(self):
        '''temp = self.head
        for i in range(self.length):
            new = temp.next
            temp.next = None
            temp = new'''
        self.head=None
        self.tail = None
        self.length = 0
        
    def reverse(self):
        prev = None
        curr = self.head
        nexte = self.head.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = nexte
            if nexte:
                nexte = nexte.next
        self.head,self.tail = self.tail,self.head
        
    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result += str(temp.value)
            if temp.next is not None:
                result += " -> "
            temp  = temp.next
        return result
