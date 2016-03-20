def insertion_Sort(l):  
    for i, item in enumerate(l):
        if item < l[0]:
            l.pop(item)
            l.insert(0,item)
        else:
            if not i==0:
                j = 0
                m = i-1
                while j<=m and item>=l[j]:
                    j = j + 1
                if not i+1 == j:
                    l.pop(i)
                    l.insert(j,item)
            
    print(l)
    
def main():
    l = [2,1,4,5,3,3,2,1]
    insertion_Sort(l)

if __name__=="__main__":main()