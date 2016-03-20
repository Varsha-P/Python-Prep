'''
Arguments are passed by assignment. The rationale behind this is twofold:
    1.) the parameter passed in is actually a reference to an object (but the reference is passed by value)
    2.) some data types are mutable, but others are not
So:

If you pass a mutable object into a method, the method gets a reference to that same object and you can mutate it,
but if you rebind the reference in the method, the outer scope will know nothing about it, 
and after you are done, the outer reference will still point at the original object.

If you pass an immutable object to a method, you still cannot rebind the outer reference, and you cannot even mutate the object
'''

def quick_sort(l, low, high):
    if l == None or len(l) == 0:
        return
    if low >= high:
        return
    middle = low + (high-low)//2
    pivot = l[middle]
    i, j = low, high
    while i<=j:
        while l[i]<pivot:
            i += 1
        while l[j]>pivot:
            j -= 1

        if i<=j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
    print(l)
    if j>low:
        quick_sort(l,low,j)
    if i<high:
        quick_sort(l,i,high)
         
def main():
    #l = [8,1,5,3,4]
    l1 = [6,5,1,3,8,4,7,9,2,]
    quick_sort(l1,0,len(l1)-1)
    #print(l)

if __name__=="__main__":main()