'''insert before
insert after
remove
concatenate two circular linkedlists
'''


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
            if current==self.head:
                current = None
    
    def __str__(self):
        #gen = (x for x in self break if x.next==self.head)
        return ' '.join([str(x) for x in self])
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        if self.head == None:
            self.head = temp 
            self.head.next = self.head
        else:
            current = self.head
            while not current.next==self.head:
                current = current.next
            current.next = temp
            temp.next = self.head
        return temp
        self.size += 1
        
        
    def remove(self,item):
        current = self.head
        if self.head.data==item:
            self.head = self.head.next
            self.size -= 1
        else:
            while not current.next==self.head:
                if item==current.next.data:
                    current.next = current.next.next
                    self.size -= 1
                    break
                else:    
                    current = current.next
                    
    def returnNodeAtBeginning(self,node):
        print()
        if node.next==node:
            return node
        if node.next.next==node:
            return node
        p1=node
        p2=node.next.next
        while not p1==p2:
            p1=p1.next
            p2=p2.next.next
        return p1

def main():
    ll = LinkedList()
    ll.add(1)
    t = ll.add(2)
    #t = ll.add(3)
    #ll.add(4)
    #ll.add(5)
    print(str(ll))
    #ll.remove(4)
    #print(str(ll))
    print(ll.returnNodeAtBeginning(t).data)
    



if __name__=="__main__":main()


