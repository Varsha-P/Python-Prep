def main():
    inputList = [str(x).lower() for x in input().split()]
    print(inputList)
    d = {}
    for item in inputList:
        if not item in d.keys():
            d[item] = 'one'
        else:
            d[item] = 'multiple'
    print(len(d.keys()))    
       
if __name__=="__main__":main()