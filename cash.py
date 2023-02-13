def isFloat(string):
    try:
        value = (float(string))         # checks if float
        if value >= 0:                  # checks if positive
            return True
    except:
        return False
# User Input
while True:
    change = input("Change owed: ")
    if isFloat(change) == True:
        change = float(change)
        break
    else:
        continue

cents = round(int(change * 100)) # turn dollars into cents
counter = 0 
while True:
    if cents >= 25:     # quarters
        cents -= 25
        counter += 1
    elif cents >= 10:   # dimes
        cents -= 10
        counter += 1
    elif cents >= 5:    # nickels
        cents -= 5
        counter += 1
    elif cents >= 1:    # pennies
        cents -= 1
        counter += 1
    else:
        break
print(counter)

    

