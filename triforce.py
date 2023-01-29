import turtle


def triforce():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t1.right(60)
    t2.left(60)
    t3.goto(100, 0)
    t3.right(60)

    for i in range(3):
        t1.forward(100)
        t1.right(360 / 3)
        t2.forward(100)
        t2.right(360 / 3)
        t3.forward(100)
        t3.right(360 / 3)
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    turtle.done()
triforce()