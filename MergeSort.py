def merge_sort(l):
    l_len = len(l)
    if len(l)==1:
        return l 
    l1 = merge_sort(l[:l_len//2])
    l2 = merge_sort(l[l_len//2:])
    l3 = []
    while len(l1)>0:
        if l2[0]<l1[0]:
            l3.append(l2[0])
            l2.pop(0)
        else:
            l3.append(l1[0])
            l1.pop(0)
        if len(l2)==0:
            while(len(l1)>0):
                l3.append(l1[0])
                l1.pop()
                break 
    while len(l2)>0:
            l3.append(l2[0])
            l2.pop(0) 
    return l3           


def main():
    l = [2,1,4,5,3]
    print(merge_sort(l))

#if __name__=="__main__":main()