def bubble_sort(m):
    print(m)
    while True:
        i = 0 
        num_of_swaps = 0
        while True:
            if m[i] > m[i+1]:
                temp = m[i]
                m[i] = m[i+1]
                m[i+1] = temp
                num_of_swaps += 1
            i = i + 1
            if i>len(m)-2:
                break
        if num_of_swaps == 0:
            break
    print(m)
    
def main():    
    l = [2,1,4,5,3,1,5,6,7,0,-10]
    bubble_sort(l)
    print(l)
    
if __name__=="__main__":main()    