import turtle

def drawshape():
    n = int(input("Number of sides: "))

    t = turtle.Turtle()

    for i in range(n):
        t.forward(100)
        t.left(360 / n)
    t.hideturtle()
    turtle.done()
drawshape()
    