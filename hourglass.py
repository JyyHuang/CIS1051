# Bonus 1 Hourglass
def hourglass():
    print("|\"\"\"\"\"\"\"\"\"\"|")
    colon = "::"
    for i in range(4,0,-1):
        for space in range(4-i):
            print(" ", end="")
        print(" \\",colon*i,"/",sep="",end="")
        print()
    print("     ||")
    for i in range(0,4,1):
        for space in range(4-i):
            print(" ", end="")
        print("/",colon*(i+1),"\\",sep="",end="")
        print()
    print("|\"\"\"\"\"\"\"\"\"\"|")

hourglass()