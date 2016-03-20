# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def main():
    sampleInput = []
    try:
        for i in range(3):
            sampleInput.append(input())
        N, M = sampleInput[0].split()
        patternBuild = ""
        for c in sampleInput[2]:
            if c=='*':
                patternBuild += "[ABCD]"
            else:
                patternBuild += c
        a_list = re.findall(patternBuild,sampleInput[1])
        print(len(a_list))
    except:
        print("Error! Something might have gone wrong with the input")
            

if __name__=="__main__":main()

