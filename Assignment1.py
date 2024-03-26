#queue using list
class Queue:
    def __init__(self):
        self.item = []
        
    def is_empty(self):
        return len(self.item)==0
    
    def enQueue(self,data):
        self.item.append(data)

    def deQueue(self):
        if self.is_empty():
            print("List is empty")
            
        else:    
            return self.item.pop(0)

    def getFront(self):
        if self.is_empty():
            print("List is empty")
            
        else:
            return self.item[0]
        
    def getRear(self):
        if self.is_empty():
            print("List is empty")
            
        else:
            return self.item[-1]
        
    def size(self):
        return len(self.item)
    
q = Queue()
print(q.is_empty())
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
print("Size of Queue:",q.size())
print("Front:",q.getFront())
print("Rear:",q.getRear())
print()
q.deQueue()
print("Size of Queue:",q.size())
print("Front:",q.getFront())
print("Rear:",q.getRear())