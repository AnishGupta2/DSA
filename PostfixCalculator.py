#Implementing Stack using Linked List
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    #Making Linked List Iterable
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head = None
        
#Defining the operations
def operation(value1,value2,operator):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1*value2
    elif operator == "/":
        if value2 == 0:
            return "Cannot Divide By Zero"
        else:
            return value1/value2
 
     
def calculator(postfixexpression):
    values=postfixexpression.split()
    stack = Stack()
    for item in values:
        if item.isdigit() == True:
            stack.push(int(item))
        elif item in "+-/*":
            if stack.isEmpty():
                return "Invalid Input"
            value2 = stack.pop()
            if stack.isEmpty():
                return "Invalid Input"
            value1 = stack.pop()
            temp = operation(value1,value2,item)
            stack.push(temp)
        else:
            return "Invalid Input"
    ans = stack.pop()
    if stack.isEmpty():
        return ans
    else:
        return "Invalid Input"

print("Instruction For Input: The Expression should be in postfix notation and each item should be divided by a space for example, 5 3 + ")
value = input("Enter the Expression: ")
print("Answer:",calculator(value))