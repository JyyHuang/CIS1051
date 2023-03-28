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
print(threearmstrong(370))

def riddler():
    for number in range(1001,10000,2):
        thou = number // 1000
        hund = number // 100  % 10
        tens = number // 10 % 10 
        ones = number % 10
        if thou != hund and thou != tens and thou != ones and hund != tens and hund != ones and tens != ones:
            if 3 * tens == thou:
                if thou + hund +tens + ones == 27:
                    return number
print(riddler())