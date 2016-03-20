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
        return '->'.join([str(item) for item in self])
        
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
        
def addNumsList(ll1,ll2):
    l1 = ll1.head
    l2 = ll2.head
    carry = 0
    result = LinkedList()
    while l1 or l2:
        if l1 and l2:
            d1 = l1.data
            d2 = l2.data
            l1 = l1.next
            l2 = l2.next
        elif l1:
            d1 = l1.data
            d2 = 0
            l1 = l1.next
        else:
            d1 = 0
            d2 = l2.data
            l2 = l2.next
        num = d1 + d2 + carry
        node = Node(num%10)
        node.next = result.head
        result.head = node
        carry = num//10
    if carry>0:
        node = Node(carry)
        node.next = result.head
        result.head = node
    return result

def addNumsListInorder(ll1,ll2):        
    s1 = ll1.size
    s2 = ll2.size
    diff = s1-s2
    diff = diff if diff>0 else -diff
    if diff!=0:
        if s1>s2:
            print()
            while diff!=0:
                node = Node(0)
                node.next = ll2.head
                ll2.head = node
                diff -= 1
        else:
            while diff!=0:
                node = Node(0)
                node.next = ll1.head
                ll1.head = node
                diff -= 1
    l1,l2,ll = ll1.head, ll2.head, LinkedList()
    num = addLL(l1,l2,ll)
    if num>0:
        node = Node(num%10)
        node.next = ll.head
        ll.head = node
    return ll

def addLL(l1,l2,ll): 
    if not l1.next and not l2.next:
        ll.add((l1.data+l2.data)%10)
        return (l1.data+l2.data)//10
    carry = addLL(l1.next,l2.next,ll)
    num = l1.data+l2.data+carry
    node = Node(num%10)
    node.next = ll.head
    ll.head = node
    return num//10
    
            
def main():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.add(9)
    ll1.add(9)
    ll1.add(9)
    ll2.add(9)
    ll2.add(9)
    print(str(addNumsList(ll1, ll2)))
    print(str(addNumsListInorder(ll1, ll2)))

if __name__=="__main__":main()


