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
        
    def aroundX(self,x):
        before = LinkedList()
        after = LinkedList()
        current = self.head
        while current:
            if current.data<x:
                before.add(current.data)
            else:
                after.add(current.data)
            current = current.next
        curr = before.head
        while curr.next:
            curr = curr.next
        curr.next = after.head 
        return before
    
def main():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(5)
    ll.add(6)
    ll.add(4)
    ll.add(3)
    ll.add(0)
    ll.add(7)
    ll.add(9)
    print(str(ll.aroundX(5)))

if __name__=="__main__":main()