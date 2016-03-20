def toSet(l):
    s = set()
    for w in l:
        for c in w:
            s.add(c)
    return s

def main():
    wordList = list(str(input()).split())
    charSet = set(str(input()).split())
    print(wordList)
    print(charSet)
    wordCharSet = toSet(wordList)
    diff = wordCharSet - charSet
    if not len(diff)==0:
        print('not contained')
    else:
        print('contained')
    
    
if __name__=="__main__":main()