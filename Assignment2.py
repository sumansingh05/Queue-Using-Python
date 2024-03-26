#Queue implementation using singly linked list concept 
class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None#this point towards self.front
        self.tail = None#this point towards self.rear
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def enQueue(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode            
        else:
            self.tail.next = newNode
        self.tail = newNode#self.rear is updated
        self.size += 1

    def deQueue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None                                               
        else:
            self.head = self.head.next#it remove a node from self.front
        self.size -= 1

    def getHead(self): #this return self.front
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        else:
            return self.head.item

    def getTail(self): #this return self.rear
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        else:
            return self.tail.item
        
    def size(self):
        return self.size
    
q = Queue()
print(q.is_empty())
q.enQueue(5)
print("Head of Queue:",q.getHead())
print("Tail of Queue:",q.getTail())

q.enQueue(10)
q.enQueue(15)                               
q.enQueue(20)
q.enQueue(25)
print("Head of Queue:",q.getHead())
print("Tail of Queue:",q.getTail())






        
