def isFloat(string):
    try:
        value = (float(string))
        if value >= 0:
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
    if cents >= 25:
        cents -= 25
        counter += 1
    elif cents >= 10:
        cents -= 10
        counter += 1
    elif cents >= 5:
        cents -= 5
        counter += 1
    elif cents >= 1:
        cents -= 1
        counter += 1
    else:
        break
print(counter)

    

