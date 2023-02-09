def isFloat(string):

# User Input
while True:
    try:
        total = input("Total amount: ")
        if isFloat(total) == True:
            break
    except:
        if isFloat(total) == False:
            continue
