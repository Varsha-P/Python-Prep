class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self):
        return ' '.join([str(item) for item in self])
    
    def backward(self):
        return ''.join(str(self)[::-1])
    
    def insert_front(self,item):
        new_node = Node(item)
        if self.head:
            current = self.head
            self.head = new_node
            new_node.next = current
        else:
            self.head = new_node
            self.tail = new_node
    
    def insert_rear(self,item):
        new_node = Node(item)
        if self.head:
            current = self.tail
            new_node.prev = current
            current.next = new_node
            self.tail = new_node            
        else:
            self.head = new_node
            self.tail = new_node  
    
    def delete_front(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        print()   
    
    def delete_rear(self):
        if self.head:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        print()    
    def delete(self,item):
        current = self.head
        if current:
            if current.data == item:
                self.head = self.head.next
                if self.head.prev:
                    self.head.prev = None
                return
            while current.next:
                if current.next.data==item:
                    if current.next==self.tail:
                        self.tail = current
                        self.tail.next = None
                        break
                    else:
                        current.next = current.next.next
                        if current.next:
                            current.next.prev = current
                        break
                else:
                    current = current.next
    
def main():
    print()
    dl = DlinkedList()
    dl.insert_front(1)
    dl.insert_rear(2)
    dl.insert_rear(3)
    dl.insert_rear(4)
    print(str(dl))
    #dl.delete_front()
    #dl.delete(3)
    dl.delete(1)
    dl.delete(4)
    print(dl.backward())
    
if __name__=="__main__":main()