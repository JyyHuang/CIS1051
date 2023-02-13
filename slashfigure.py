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

slashfigure(6)