import turtle
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

#Slash Figure
def slashfigure(n):
    exclamation = "!"
    backslash = "\\"
    slash = "/"
    step = (n*4)-2
    counter = 0
    for i in range(0,n):
        print(backslash*counter, exclamation*step, slash*counter, sep="")
        step = step - 4
        counter = counter + 2


def drawNgon(myTurtle, numSides, sideLength):
    for i in range(numSides):
        myTurtle.fd(sideLength)
        myTurtle.left(360 / numSides)
# Super Duper Spiral
def superduperspiral(myTurtle, numSides, sideLength, numShapes):
    color = ["red", "green", "blue"]
    for i in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.right(8)
        myTurtle.color(color[i%3])
    turtle.done()
    
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
#turtle.bgcolor("black")
#drawNgon(t, 6, 100)
#hourglass()
#slashfigure(6)
#superduperspiral(t, 6, 100, 50)