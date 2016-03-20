import sys

def main():
    stuartWords = 0
    kevinWords = 0
    vowels = {'A': 1,'E': 2,'I': 3,'O': 4,'U': 5}
    inputString = sys.argv(1)  
    length = len(inputString)
    counter = 0
    for e in inputString:
        counter += 1
        if(e in vowels.keys()):
            kevinWords = kevinWords + length - counter + 1
            
        else:
            stuartWords = stuartWords + length - counter + 1
    if(stuartWords>kevinWords):
        print("Stuart",format(stuartWords))      
    elif(kevinWords>stuartWords):
        print("Kevin",format(kevinWords))
    else:
        print("Draw")
    
if __name__=="__main__":main()