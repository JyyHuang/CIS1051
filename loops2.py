def vowels(string):
    counter = 0
    for i in string:
        if i in ["a","e","i","o","u"]:
            counter += 1
    return counter


#print(vowels("hello"))

def evendigits(int):
    arr = []
    counter = 0
    for i in range(1, len(str(int))+1):
        arr.append(int % (10**i) // 10**(i-1))
    for i in arr:
        if i % 2 == 0:
            counter += 1
    return counter

#print(evendigits(12345))


def threearmstrong(int):
    arr = []
    arr2 = []
    for i in range(1, len(str(int))+1):
        arr.append(int % (10**i) // 10**(i-1))
    for i in arr:
        arr2.append(i**3)
    if sum(arr2) == int:
        return True
    else:
        return False
#print(threearmstrong(370))

def riddler():
    arr = []
    for i in range(1000, 10000):
        arr.append(i)
    for i in arr:
        if i % 10 != (i % 100 // 10) != (i % 1000 // 100) != (i % 10000 // 1000):
            if (i % 10000 // 1000) * 3 == (i % 100 // 10):
                if i % 2 != 0:
                    if (i % 10) + (i % 100 // 10) + (i % 1000 // 100) + (i % 10000 // 1000) == 27:
                        return i

print(riddler())