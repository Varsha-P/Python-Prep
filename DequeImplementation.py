'''
Maintain a HEAD node, which stores both front and rear nodes 
which can be used to represent the same structure
ie., the same data structure is being referenced by two variables if we have front and rear.
Instead, maintain a HEAD node 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None
        self.prev = None
        
class Deque:
    def __init__(self):
        self.head = None
        self.rear = None
        self._size = 0
        
    def push_front(self, data):
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
            self.rear = new_Node
        else:
            new_Node.nxt = self.head
            self.head.prev = new_Node
            self.head = new_Node
        self._size += 1
    
    def pop_front(self):
        ret = None
        if not self.head==None:
            ret = self.head.data
            if self._size==1:
                self.head = None
                self.rear = None
            else:
                self.head = self.head.nxt
                self.head.prev = None
            self._size -= 1
        else:
            print('No elements to pop!')
        return ret
            
    def push(self, data):        
        new_Node = Node(data)
        if not self.head:
            self.head = new_Node
            self.rear = new_Node
        else:
            new_Node.prev = self.rear
            self.rear.nxt = new_Node
            self.rear = new_Node
        self._size += 1
    
    def pop(self):
        ret = None
        if not self.head==None:
            ret = self.rear.data
            if self._size==1:
                self.head = None
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.nxt = None
            self._size -= 1
        else:
            print('No elements to pop!')
        return ret
    
    def peek_rear(self):
        if not self.head:
            print('No elements in deque!')
        else:
            return self.rear.data
    
    def peek(self):
        if not self.head:
            print('No elements in Deque!')
        else:
            return self.head.data
        print()
    
    def size(self):
        return self._size
    
    def __iter__(self):
        """Return iterator for the stack."""
        current = self.head
        while current:
            yield current.data
            current = current.nxt    
         
    def __str__(self):
            return (' '.join([str(item) for item in self]))
        
def main():
    deq = Deque()
    deq.push_front(1)
    deq.push_front(2)
    deq.push_front(3)
    deq.push(4)
    print(str(deq))
    print(deq.pop_front())
    print(deq.pop())
    print(str(deq))
    
if __name__=="__main__":main()
