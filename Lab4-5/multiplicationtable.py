#Multiplication Table
def multiplicationtable(size):
    for row in range(1, size+1): # 1-5
        print()
        for col in range(1, size+1): # 1-5
            print(row*col, end="\t")
    print()


multiplicationtable(4)