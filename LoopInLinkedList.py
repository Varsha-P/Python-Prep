class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None 
        self.size = 0 
        
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self):
        return ' '.join([str(item) for item in self])
        
    def isEmpty(self):
        return self.head == None
        
    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp 
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = temp
        self.size += 1
        
        
def main(): 
    ll = LinkedList()
          
        
if __name__=="__main__":main()



