# 99 bottles of beer
def bottlesofbeer(beers):
    for i in range(beers, 0, -1): 
        print(beers, "bottle of beer on the wall,", beers, "bottles of beer")
        print("Take one down, pass it around,", beers-1,"bottles of beer on the wall") # prints -1 bottles
        print()
        beers -= 1 # decreases bottles by 1 every iteration

bottlesofbeer(10)