class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        return " ".join([str(x) for x in self])
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    def add(self,data):
        current = self.head
        if not current:
            self.head = Node(data)
        else:
            while current.next:
                current = current.next
            current.next = Node(data)
    def kthToLastIter(self,k):
        p1, p2 = self.head, self.head
        count = 0
        while count<k:
            count += 1
            p2 = p2.next
        count = 0
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        print(p1.data)
        #print(p2.data)
    def kthToLastIter2(self,k):
        current = self.head
        n = 0
        while current.next:
            n += 1
            current = current.next
        count = 0
        current = self.head
        while count<n-k:
            current = current.next
            count += 1
        return current
        
    def kthToLastRec(self,node,k):
        if not node.next:
            return 0
        count = self.kthToLastRec(node.next,k)+1
        if count==3:
            print(node.data)
        return count
    
    
    
def main():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    print(str(ll))
    ll.kthToLastIter(3)
    ll.kthToLastRec(ll.head,3)
    print(ll.kthToLastIter2(3).data)

if __name__=="__main__":main()