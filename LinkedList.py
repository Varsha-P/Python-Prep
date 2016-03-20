'''Do this operation:    Concatenate two linkedlists
have to make sure size is maintained right'''

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
        
        
    def remove(self,item):
        current = self.head
        if self.head.data==item:
            self.head = self.head.next
            self.size -= 1
        else:
            while current.next:
                if item==current.next.data:
                    current.next = current.next.next
                    self.size -= 1
                    break
                else:    
                    current = current.next
            
    def search(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                print('Found!')
                return item
                break
            else:
                current = current.next
        print('Not found!')
        return None
        
        
mylist = LinkedList()   
mylist.add(31)
mylist.add(77)
mylist.add(35)
mylist.add(67)
mylist.add(1)
mylist.add(2)
mylist.add(18)
mylist.add(999)
print(str(mylist))
print(mylist.size)
mylist.remove(67)
print(mylist.size)
mylist.remove(31)
print(mylist.size)
print(str(mylist))
mylist.search(999)
mylist.search(9)
#print(mylist.head.getData())
#print(mylist.size())
#print(mylist.search(1))
#print(mylist.search(18))
