# Stairs
    # DrawSquare
        # myTurtle is the turtle doing the drawing
        # size is the length of each of the sides of the square.
import turtle

Size = int(input("How many pixels on each side? "))
t = turtle.Turtle()

def drawSquare(myTurtle, squareSize):
    for i in range(4):
        myTurtle.fd(squareSize)
        myTurtle.right(90)
drawSquare(t, Size)


    # Drawing a Row of Squares
        # draws a row of squares
        # myTurtle is the turtle doing the drawing
        # length is how many squares are in the row
        # squareSize is the length of each of the sides of each square.
squares = int(input("How many squares? "))
Size = int(input("How many pixels on each side? "))
def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        drawSquare(myTurtle, squareSize)
        myTurtle.fd(squareSize)
drawRow(t, squares, Size)

    
    # Drawing a Grid
        # myTurtle is the turtle doing the drawing
        # the grid will be "size" squares wide and "size" squares tall
        # squareSize is the length of each of the sides of each individual square.
def drawGrid(myTurtle, size, squareSize):
    for i in range(size):

