
'''handle equal to CASE'''
'''INCREASE_KEY'''
def insert_item(A, item):
    l = len(A)
    A.append(item)
    parent = (l-1)//2   
    if not A[parent]>=item:
        max_heapify(A, parent, l)
    
def max_heapify(A,index,max_i):
    a_i = index
    if 2*a_i+1<=max_i:
        left_child = A[2*a_i+1]
    else:
        left_child = False
    if 2*a_i+2<=max_i:
        right_child = A[2*a_i+2]
    else:
        right_child = False
    if left_child and right_child:
        left_child_index = 2*a_i+1
        right_child_index = 2*a_i+2
        if left_child > right_child:
            A[2*a_i+1] = A[a_i]
            A[a_i] = left_child
            if 2*left_child_index+1 <= max_i:
                if 2*left_child_index+2 <= max_i:
                    if not(A[left_child_index]>A[2*left_child_index+1] and A[left_child_index]>A[2*left_child_index+2]):
                        max_heapify(A, left_child_index, max_i)
                else:
                    if not(A[left_child_index]>A[2*left_child_index+1]):
                        max_heapify(A, left_child_index, max_i)
                                       
        else:
            A[2*a_i+2] = A[a_i]
            A[a_i] = right_child 
            if 2*right_child_index+1 <= max_i:
                if 2*right_child_index+2 <= max_i:
                    if not(A[right_child_index]>A[2*right_child_index+1] and A[right_child_index]>A[2*right_child_index+2]):
                        max_heapify(A, right_child_index, max_i)
                else:
                    if not(A[right_child_index]>A[2*right_child_index+1]):
                        max_heapify(A, right_child_index, max_i)       
    else:
        if left_child > A[a_i]:
            A[2*a_i+1] = A[a_i]
            A[a_i] = left_child

def build_max_heap(B):
    print(B) 
    n = len(B)
    i = n//2  
    while i>=0:
        max_heapify(B, i, n-1)
        i -= 1 
        
def heap_sort(B):
    l = len(B)-1
    if l==0:
        print(l[0])
    else:
        while True:
            temp = B[0]
            B[0] = B[l] 
            B[l] = temp
            print(B.pop())
            l = len(B)-1 
            if l==0:
                print(B[0])
                break
            max_heapify(B, 0, l)
    
def return_max(A):
    if len(A):  
        return A[0] 
    
def extract_max(B):
    if len(B)>2:
        l = len(B)-1
        temp = B[0]
        B[0] = B[l] 
        B[l] = temp
        x = B.pop()
        l = len(B)-1 
        max_heapify(B, 0, l)
        return x
    elif len(B)==2 or len(B)==1:
        return B.pop()
    else:
        print('No elements in heap')
    
    
        
def main():
    #A = [16,14,10,8,1,9,3,2,4,7,]
    #max_heapify(A,4,9)
    B = [1,4,5,6,2,9,15,12,24,22,29]
    build_max_heap(B)
    #print('right order [16,14,10,8,7,9,3,2,4,1]')
    #print(B) 
    #print('max is: {0}'.format(B[0]))   
    #print(return_max(B))
    insert_item(B, 7)
    insert_item(B, 8)
    insert_item(B, 10)
    extract_max(B)
    heap_sort(B)
    
if __name__=="__main__":main()
