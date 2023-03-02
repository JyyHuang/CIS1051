import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    t.penup()
    with open("data/irma.csv", "r") as irmafile:
        for lines in irmafile.readlines()[1:]: # from second line
            lines = lines.split(",")    # splits each line into arrays for each value in that line
            lat = float(lines[2])
            lon = float(lines[3])
            wind = float(lines[4])


            if wind < 74:               # no hurricane strength
                t.pencolor("white")
                t.width(1)
            elif 74 <= wind <= 95:      # category 1
                t.pencolor("blue")
                t.width(4)
                t.write("1", font=("Arial",15))
            elif 96 <= wind <= 110:     # category 2
                t.pencolor("green")
                t.width(7)
                t.write("2", font=("Arial",15))
            elif 111 <= wind <= 129:    # category 3
                t.pencolor("yellow")
                t.width(10)
                t.write("3", font=("Arial",15))
            elif 130 <= wind <= 156:    # category 4
                t.pencolor("orange")
                t.width(14)
                t.write("4", font=("Arial",15))
            else:                       # category 5
                t.pencolor("red")
                t.width(19)
                t.write("5", font=("Arial",15))
            t.goto(lon, lat)
            t.pendown()

    turtle.done()
if __name__ == "__main__":
    irma()
