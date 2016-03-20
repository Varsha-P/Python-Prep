''' Using a List
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item) # or self.items.insert(0,item)

     def pop(self):
         return self.items.pop() # or self.items.pop(0)

     def peek(self):
         return self.items[len(self.items)-1] # or self.items[0]

     def size(self):
         return len(self.items)'''
         
 
'''Using a linkedlist'''        
class Node():
    """An internal class that represents a node with a single item
    and a link to the next node.
    """

    def __init__(self, item):
        self.item = item
        self.next = None


class Stack():
    """An implementation of a simple stack with linked list."""
    def __init__(self):
        """Initialize an empty stack."""
        self._top = None
        self._size = 0

    @property
    def size(self):
        """The number of items in the stack."""
        return self._size

    def isEmpty(self):
        """Check if the stack is empty.

        Returns:
            True if the stack is empty.
            False otherwise.
        """
        return self._size == 0

    def push(self, item):
        """Insert an item to the stack."""
        n = Node(item)
        n.next = self._top
        self._top = n
        self._size += 1

    def pop(self):
        """Remove and return the last added item from the stack.

        Returns:
            The last item added to the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        n = self._top
        self._top = self._top.next
        self._size -= 1
        return n.item

    def peek(self):
        """Return the last added item from the stack.

        Returns:
            The last item added to the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self._top.item

    def __iter__(self):
        """Return iterator for the stack."""
        current = self._top
        while current:
            yield current.item
            current = current.next

    def __str__(self):
        """String representation of the stack."""
        return " ".join(reversed([str(item) for item in self]))


if __name__ == "__main__":
    print("Stack using linked list.")
    s = Stack()
    print('Stack:'+str(s))
    while True:
        n = str(input("Enter a number to enter or pop to pop a number"
                          "(exit when stack empty): "))
        if n=='pop': # TRUTH VALUE OF ZERO(0) IS FALSE
            if s.isEmpty():
                print("Stack is empty. ")
                continue
            print("Popped: " + str(s.pop()))
            print("Current stack: " + str(s))
        elif n=='exit':           
            break
        else:  
            try: 
                s.push(int(n))
                print("Pushed: " + str(s.peek()))
                print("Current stack: " + str(s))
            except:
                print('Not valid input! Please re-enter')
            