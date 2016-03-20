import collections

def main():
    N = int(input())
    patients = collections.OrderedDict()
    for i in range(N):
        l = list(str(input()).split(':'))
        if l[1] in patients.keys():
            patients[l[1]].append(l[0])
        else:
            patients[l[1]] = [l[0]]
    for ssn in patients:
        l = patients[ssn]
        if len(l)==1:
            print(l[0]+':'+ssn)
        else:                
            firstName, lastName, middleName = '', '', ''
            for name in l:
                lastnameFirst = name.split(',')
                if len(lastnameFirst)>1:
                    lastName = ' '+lastnameFirst[0]
                    firstMiddle = lastnameFirst[1].split()
                    if len(firstMiddle)>1:
                        firstName = firstMiddle[0]
                        middleName = ' '+firstMiddle[1]
                    else:
                        firstName = lastnameFirst[1]
                            
            print(firstName+middleName+lastName+':'+ssn)            
    
if __name__=="__main__":main()