# Stairs
import turtle
    # DrawSquare
        # myTurtle is the turtle doing the drawing
        # size is the length of each of the sides of the square.
def drawSquare(myTurtle, squareSize):
    for i in range(4):
        myTurtle.fd(squareSize)
        myTurtle.right(90)

    # Drawing a Row of Squares
        # draws a row of squares
        # myTurtle is the turtle doing the drawing
        # length is how many squares are in the row
        # squareSize is the length of each of the sides of each square.
def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        drawSquare(myTurtle, squareSize)
        myTurtle.fd(squareSize)
    
    # Drawing a Grid
        # myTurtle is the turtle doing the drawing
        # the grid will be "size" squares wide and "size" squares tall
        # squareSize is the length of each of the sides of each individual square.
def drawGrid(myTurtle, size, squareSize):
    for row in range(size):
        drawRow(myTurtle, size, squareSize)
        myTurtle.backward(squareSize * size)
        myTurtle.right(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)

# myTurtle is the turtle doing the drawing
# height is how tall the stairs are going to be
# squareSize is the length of each of the sides of each square.
def drawSquareStairs(myTurtle, height, squareSize):
    num = height - 1
    for row in range(height):
        drawRow(myTurtle, height - num, squareSize)
        myTurtle.backward(squareSize * (height - num))
        myTurtle.right(90)
        myTurtle.fd(squareSize)
        myTurtle.left(90)
        height += 2
        num += 1


# Spirals
    #myTurtle is the turtle doing the drawing
    #numSides is num sides on the polygon
    #sideLength is the length of sides
def drawNgon(myTurtle, numSides, sideLength):
    for i in range(numSides):
        myTurtle.fd(sideLength)
        myTurtle.left(360 / numSides)

    # draws a spiral of shapes.
    # this is done by drawing a single polygon, rotating the turtle a bit,
    # drawing another polygon until the spiral is completed.
    # numSides defines the shape of the polygons
    # sideLength defines how big each polygon is
    # numShapes defines how many polygons make up the spiral
def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    for i in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.right(8)
    turtle.done()


t = turtle.Turtle()
t.speed(10)
#drawSquare(t, 50)
#drawRow(t, 5, 50)
#drawGrid(t, 5, 50)
#drawSquareStairs(t, 5, 50)
#drawNgon(t, 6, 100)
drawNgonSpiral(t, 6, 100, 40)