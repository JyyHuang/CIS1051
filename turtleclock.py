import turtle

def turtleclock():
    t = turtle.Turtle()
    t.shape("turtle")
    t.color("black")
    moveright = 30
    moveleft = -30
    for i in range(12):
        t.penup()
        t.forward(100)
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(10)
        t.stamp()
        t.home()
        if moveright <= 180:
            t.rt(moveright)
            moveright += 30
        else:
            t.rt(moveleft)
            moveleft -= 30
    t.hideturtle()
    turtle.done()
turtleclock()