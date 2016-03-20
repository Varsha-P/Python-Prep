''' handle equal to CASE'''
''' BST delete-- node with two children-- either replace node with largest number on left subtree or with smallest node on right subtree
Then delete the respective largest or smallest number'''

class Node:
    def __init__(self,value):
        self.data = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        
class BST:   
    def __init__(self):
        self.root = None
        self.node = None
             
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
            self.node = self.root
        else:
            if data<self.node.data:
                if self.node.left_child:                    
                    self.node = self.node.left_child
                    self.insert(data)
                else:
                    self.node.left_child = Node(data)
                    self.node.left_child.parent = self.node
                    self.node = self.root
            else:
                if self.node.right_child:
                    self.node = self.node.right_child
                    self.insert(data)
                else:
                    self.node.right_child = Node(data)
                    self.node.right_child.parent = self.node
                    self.node = self.root
        
    def inorder_traversal(self):
        if self.root is None:
            print('Tree is empty!')
            return ''
        l = []
        st = []
        current = self.root
        if self.root is None:
            return l
        while current or not len(st)==0:
            while current:
                st.append(current)
                current = current.left_child
            current = st.pop()
            l.append(current.data)
            current = current.right_child
        print(' '.join(str(i) for i in l))
        return l
    
    def lookup_recursive(self, node1, data, parent=None):
        if data < node1.data:
            if node1.left_child is None:
                return None, None
            return self.lookup(node1.left_child, data, node1)
        elif data > node1.data:
            if node1.right_child is None:
                return None, None
            return self.lookup(node1.right_child, data, node1)
        else:
            return node1, parent
        
    def lookup_iterative(self,node1,data,parent=None):
        current_node = node1
        while current_node:
            if data==current_node.data:
                return current_node, current_node.parent
            if data<current_node.data:
                current_node=current_node.left_child
            else:
                current_node=current_node.right_child
                if not current_node:
                    print('Element not present')
                    break
        return None, None
        
    def children_count(self,node):
        """Return the number of children
        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if node.left_child:
            cnt += 1
        if node.right_child:
            cnt += 1
        return cnt
    
    def print_tree(self,node): 
        """ Alternate to inorder function
        Print tree content inorder
        """
        if node.left_child:
            self.print_tree(node.left_child)
        print(node.data, end=" ")
        if node.right_child:
            self.print_tree(node.right_child)
            
    def delete(self, data):
        """Delete node containing data
        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup_iterative(self.root,data)
        #self.remove_node(node)
        if node is not None:
            children_count = self.children_count(node)
            #print(children_count)
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left_child is node:
                        parent.left_child = None
                    else:
                        parent.right_child = None
                else:
                    self.root = None
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left_child:
                    n = node.left_child
                else:
                    n = node.right_child
                if parent:
                    if parent.left_child is node:
                        parent.left_child = n
                        n.parent = parent
                    else:
                        parent.right_child = n
                        n.parent = parent
                else:
                    self.root.left_child = n.left_child
                    self.root.right_child = n.right_child
                    self.root.data = n.data
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right_child
                while successor.left_child:
                    parent = successor
                    successor = successor.left_child
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left_child == successor:
                    parent.left_child = successor.right_child
                else:
                    parent.right_child = successor.right_child
    def replace_node(self, node, new_node):
        """
        Replace the node by new_node, update in its parent node

        @param node: node to replace
        @param new_node: the new node
        @return: null
        """
        # special case: replace the root
        if node == self.root:
            self.root = new_node
            return
        parent = node.parent
        if parent.left_child and parent.left_child == node:
            parent.left_child = new_node
        elif parent.right_child and parent.right_child == node:
            parent.right_child = new_node
        else:
            print("Incorrect parent-children relation!")
            raise RuntimeError
        
    def remove_node(self, node):
        if node.left_child and node.right_child:    # the node has two children
            # Find its in-order successor
            successor = node.right_child
            while successor.left_child:
                successor = successor.left_child
            # Copy the node
            node.data = successor.data
            # Remove the successor
            self.remove_node(successor)
        elif node.left_child:     # the node only has a left child
            self.replace_node(node, node.left_child)
        elif node.right_child:    # the node only has a right child
            self.replace_node(node, node.right_child)
        else:               # the node has no children
            self.replace_node(None)
    ''''static int height(Node node)
    {
        /* base case tree is empty */
        if (node == null)
            return 0;
 
        /* If tree is not empty then height = 1 + max of left
           height and right heights */
        return (1 + Math.max(height(node.left), height(node.right)));
    }'''
    def height(self,node):
        if node==None:
            return 0
        return 1+max(self.height(node.left_child),self.height(node.right_child))
     
               
def main():
    A = [7,2,6,9,7,1,4,0,5,]
    bst = BST()
    for num in A:
        bst.insert(num)
    #bst.inorder_traversal(bst.root)
    #node1, parent = bst.lookup(bst.root,6)
    print(bst.height(bst.root))
    bst.inorder_traversal()    
    bst.delete(6)
    bst.inorder_traversal()
    bst.delete(9)
    bst.inorder_traversal()
    bst.delete(9)
    bst.inorder_traversal()
    bst.delete(4)
    bst.inorder_traversal()
    #bst.print_tree(bst.root)
    
if __name__=="__main__":main()
