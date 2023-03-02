import turtle
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
t.speed(0)
turtle.colormode(255)
#turtle.bgcolor("black")
#drawNgon(t, 6, 100)
#drawNgonSpiral(t, 6, 100, 50)