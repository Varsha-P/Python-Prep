import random

'''def rand7():
    r = 22
    while r>=21:
        a = random.randrange(1,5) -1
        b = random.randrange(1,5) -1
        r = 5*b +a
    return r%7 +1'''

def rand7():
    vals = [
        [ 1, 2, 3, 4, 5 ],
        [ 6, 7, 1, 2, 3 ],
        [ 4, 5, 6, 7, 1 ],
        [ 2, 3, 4, 5, 6 ],
        [ 7, 0, 0, 0, 0 ]
    ]
    result = 0
    while result==0:
        i = random.randrange(1,5)
        j = random.randrange(1,5)
        result = vals[i-1][j-1]
    return result    

def main():
    print(rand7())

if __name__=="__main__":main()
