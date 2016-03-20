def main():
    inputList = [int(x) for x in input().split()]
    d = {}
    b = True
    for i, item in enumerate(inputList):
        if not item in d.keys():
            d[item] = i
        else:
            b = False
            print(item)
    if b:
        print("No duplicates") 
              
if __name__=="__main__":main()