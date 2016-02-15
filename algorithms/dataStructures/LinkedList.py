class Node():
    def __init__(self, data, next_= None):
        self.data = data
        self.next = next_
        
    

class LinkedList():
    
    def __init__(self, head=None):
        self.head = head 
    
    def insert_end(self, data, next_=None):
        n = Node(data, next_)
        # base case
        if self.head==None:
            self.head = n
            
        # transverse linked list until the end is reached
        else:
            c = self.head
            while c.next != None:
                c = c.next
      
            c.next = n
            
    def insert_start(self, data):
        n = Node(data,self.head)
        self.head = n
        
    def insert(self, data, position):
        
        n = Node(data)
            
        # empty list
        if self.head==None:
            self.head = n
          
        # insert at head
        elif position==0:
            n.next = self.head
            self.head = n
          
        # transverse linked list until the position is reached
        else:
            curNode = self.head;
            pos=1
            
            while pos < position:
                  curNode = curNode.next
                  pos += 1
              
            n.next = curNode.next
            curNode.next = n
              
    def delete(self, position):
        
        if position==0:
            self.head = self.head.next
        
        else:
            curNode = self.head
            pos = 1
            while pos<position:
                curNode = curNode.next
                pos += 1
                
            curNode.next = curNode.next.next
    

    def display(self):
        curNode = self.head
        while curNode:
            print(curNode.data)
            curNode = curNode.next