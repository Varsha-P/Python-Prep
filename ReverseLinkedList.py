# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#     
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def __iter__(self):
#         current = self.head
#         while current:
#             yield current.data
#             current = current.next
#     def __str__(self):
#         return ' '.join([str(item) for item in self])
#     
#     def add(self,data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node
#     def reverseLinkedList(self,node):
#         print()
#         p1 = node
#         if not p1.next:
#             self.head = p1
#             return p1
#         x = self.reverseLinkedList(p1.next)
#         x.next = p1
#         p1.next = None
#         return p1        
#         
#     
# def main():
#     l = LinkedList()
#     l.add('A')
#     l.add('B')
#     l.add('C')
#     print(str(l))
#     l.reverseLinkedList(l.head)
#     print(str(l))
#     
# if __name__=="__main__":main()
#         

''' ALT Solution:

Create empty list. Traverse through main list and insert node 
encountered at beginning of list that we created earlier'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        return ' '.join([str(x) for x in self])
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
    def reverseList(self,node):
        if not node.next: 
            self.head = node
            return node
        n1 = self.reverseList(node.next)  
        n1.next = node
        node.next = None
        return node
            
def main():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    print(str(ll))
    ll.reverseList(ll.head)
    print(str(ll))
if __name__=="__main__":main()







































