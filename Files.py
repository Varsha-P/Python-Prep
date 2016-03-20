def main():
    print()
    #path ="C:/Users/varsha/Desktop/Varsha_Pattipati_8244565758/abc.txt"
    path = r"C:\Program Files\abc.txt"
    with open(path,'r') as file:
        for line in file:
            print(line,end='')
    

if __name__=="__main__":main()