
def main():
#     print("Hey")
#     inputString = str(input())
#     string1 = inputString[::-1]
#     string2 = ''.join(string1)
#     print(string2)
    print(1)
    inputString = list(input())
    last = len(inputString)-1
    for i, item in enumerate(inputString):
        temp = inputString[last-i]
        inputString[last-i] = item
        inputString[i] = temp
        
    print(inputString)    
    
if __name__=="__main__":main()    