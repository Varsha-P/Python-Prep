import fileinput

def main():
    for line in fileinput.input():
        inputString = line
        break
    if('P' in inputString):
        z=inputString.split(':')
        hrs = int(z[0]) + 12
        ind = inputString.index('P')
        time = str(hrs) +':'+ inputString[2:ind]
        print(time)
    else:
        ind = inputString.index('A')
        print(inputString[0:ind])
        
    
        
if __name__=="__main__":main()