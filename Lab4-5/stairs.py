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


#t = turtle.Turtle()
#t.speed(0)
#drawSquare(t, 50)
#drawRow(t, 5, 50)
#drawGrid(t, 5, 50)
#drawSquareStairs(t, 5, 50)
