def returnAnswer(inputList,k):
    d = {}
    print(inputList[0])
    for dictKey in inputList:
        #dictKey = int(dictKey)
        dictValue = k - dictKey
        d[dictKey] =  dictValue
    for key in d:
        if d[key] in d.keys():
            return [True, key, d[key]]
    return [False,0,0]
def main():
    inputList = [int(x) for x in input().split()]
    k = int(input())
    l = returnAnswer(inputList, k)
    if not l[0]:
        print("No numbers")
    else:
        print(l[1:])
    
if __name__=="__main__":main()    

#[15,9,7,11,70,19,75,8]