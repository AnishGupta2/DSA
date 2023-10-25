class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList:
    #Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    #Append in CSLL
    def append(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            newnode.next = newnode
            self.length += 1
        else:
            self.tail.next = newnode
            newnode.next = self.head
            self.tail = newnode
            self.length +=1
            
    #prepend in CSLL
    def prepend(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
            newnode.next = newnode
            self.length += 1
        else:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = newnode
            self.length += 1
    
    #Insert in CSLL
    def insert(self,index,value):
        newnode = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = newnode
                self.tail = newnode
                newnode.next = newnode     
            
            else:
                newnode.next = self.head
                self.head = newnode
                self.tail.next = newnode
                
        elif index == self.length:
            self.tail.next = newnode
            self.tail = newnode
            newnode.next = self.head
        
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode
        self.length += 1      
            
    
    #Search,Get,Set
    
    #Popfirst
    def popfirst(self):
        popped = self.head
        if self.length == 0:
            return None
        elif self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped.next = None
        self.length = self.length -1
        return popped
        
    def pop(self):
        if self.length == 0:
            return None
        popped = self.tail
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            popped.next = None
            self.tail = temp

        self.length = self.length - 1
        return popped
    
    #remove
    def remove(self,index):
        if index == 0:
            popfirst()
        else:
            temp = self.head
            for i in range(index -1):
                temp = temp.next
            popped = temp.next
            temp.next = popped.next
            popped.next = None
            self.length -= 1
            return popped
    
    def deleleall(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
            
    #Printing CSLL
    def __str__(self):
        result = ""
        temp = self.head
        while temp is not None:
            result = result + str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result = result + " --> "
        return result
        
    
    
    
    
    
a = CSLinkedList()
for i in range(4):
    a.append(i+1)
a.insert(4,8)
a.popfirst()
a.pop()
a.remove(2)
print(a.length)
print(a)
