def buildTree(k,valArray):
    newArray = []
    root of tree is K
    nodes at depth 1 are 1-dimensional, those at depth 2 are 2-dimensional etc.,
    for each val in valArray:
        create children when necessary and in order 
        maintain a variable at each node to keep track of its existence in the Array(Boolean Value)
    Traverse the tree using Breadth-First-Traversal and append elements to newArray  
    return newArray

def main():
    listOfLists = [] #input list of multidimensional lists
    d = {}
    finalOrderedList = []
    for aList in listOfLists:
        a = chars before '[' in aList # ie., variable name used for list
        index = chars between '[' and ']'
        #can use a regex to identify list name 'a' and 'index'
        if a in d:
            d[a].append(index)
        else:
            d[a] = aList
    for key in sorted(d.keys()): #sorting keys ie., list names
        l = buildTree(key,d[key]) #build a tree for d[key] and return ordered elements   
        finalOrderedList.append(l) # appending ordered list obtained from each tree
    print(finalOrderedList)
        
if __name__=="__main__":main()