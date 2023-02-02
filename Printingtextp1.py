# 99 bottles of beer
def bottlesofbeer(beers):
    for i in range(beers, 0, -1): 
        print(beers, "bottle of beer on the wall,", beers, "bottles of beer")
        print("Take one down, pass it around,", beers-1,"bottles of beer on the wall") # prints -1 bottles
        print()
        beers -= 1 # decreases bottles by 1 every iteration
bottles = int(input("How many bottles of beer? "))
if bottles > 99:
    print("Too many bottles of beers on the wall")
    exit()
bottlesofbeer(bottles)


#Multiplication Table
def multiplicationtable(size):
    for row in range(1, size+1): # 1-5
        print()
        for col in range(1, size+1): # 1-5
            print(row*col, end="\t")
    print()
n = int(input("Size of table? "))
multiplicationtable(n)

#Summation of Squares
def summation(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum
n = int(input("Int: "))
print(summation(n))