'''
Question:    Integer MAXSIZE
Answer:      The sys.maxint (in python2) constant was removed, since there is no longer a limit to the value of integers in python3. 
             However, sys.maxsize can be used as an integer larger than any practical list or string index. 
             It conforms to the natural integer size of the implementation and is typically the same as sys.maxint in previous releases on the same platform.

Question:    HOW BIG CAN A PYTHON LIST GET?
Answer:     a.) According to the source code, the maximum size of a list is PY_SSIZE_T_MAX/sizeof(PyObject*).
            PY_SSIZE_T_MAX is defined in pyport.h to be ((size_t) -1)>>1
            On a regular 32bit system, this is (4294967295 / 2) / 4 or 536870912.
            Therefore the maximum size of a python list on a 32 bit system is 536,870,912 elements.
            As long as the number of elements you have is equal or below this, all list functions should operate correctly.
            
            b.) The only real limit comes from the amount of memory you have and how your system stores memory references. 
            There is no per-list limit, so Python will go until it runs out of memory. 
            If you are running on an older OS or one that forces processes to use a limited amount of memory, 
            you may need to increase the amount of memory the Python process has access to.
'''

import sys
class Node:
    """An internal class that represents a node with a single item
    and a link to the next node.
    """
    def __init__(self, item):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self._size = 0
                        
    def __str__(self):
        """String representation of the stack."""
        return " ".join([str(item) for item in self])
    
    def __iter__(self):
        """Return iterator for the stack."""
        current = self.head
        while current:
            yield current.item
            current = current.next
    def size(self):
        return self._size
    def isempty(self):
        if self._size == 0:
            return True
        else:
            return False
            
    def enqueue(self, item):
        if self._size >= sys.maxsize:
            print('Limit reached!')
        else:
            new_Node = Node(item)
            self._size = self._size +1
            if self.head is None:
                self.head = new_Node
                self.head.next = None
            else:
                current = self.head
                while True:
                    if current.next is None:
                        current.next = new_Node
                        new_Node.next = None
                        break
                    else:
                        current = current.next 
        
    def dequeue(self):
        if self.isempty():
            print('Queue is empty. Operation cannot be performed!')
        else:
            self.head = self.head.next
            self._size = self._size - 1
            print(self.__str__())
        
    def peek(self):
        if self.isempty():
            print('Queue is empty!')
        else:
            print(self.head.item)

if __name__=="__main__":
    q = Queue()
    print(~2)
    while True:
        n = str(input("Please enter an integer to enqueue or deq to dequeue, peek to peek and exit to exit: "))
        if n=='exit':
            break
        elif n=='deq':
            q.dequeue()
        elif n=='peek':
            q.peek()
        else:
            try:
                q.enqueue(int(n))
                print('Current Queue: '+str(q))
            except:
                print('Invalid input!')
