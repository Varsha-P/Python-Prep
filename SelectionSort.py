def selection_sort(l):
    print(l)
    for i, item in enumerate(l):
        minimum = item
        min_index = i
        found = False
        for j, item2 in enumerate(l[i+1:]):
            if item2<minimum:
                found = True
                minimum = item2
                min_index = j + i + 1
        if found:
            temp = item
            l[i] = minimum
            l[min_index] = temp
    print(l)   
            

def main():
    l = [2,1,4,5,3,-5,-9,10]
    selection_sort(l)

if __name__=="__main__":main()
