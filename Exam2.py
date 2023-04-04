def isVowel(string):
    if string not in ("aeiou"):
        return False
    return True


def mostVowels(list):
    counter = 0
    highestword = ""
    highestcount = 0
    for word in list:
        for letter in word:
            if isVowel(letter) == True:
                counter += 1
                if counter > highestcount:
                    highestcount = counter
                    highestword = word
        counter = 0
                    
    return highestword




def oddsToZero(list):
    for index, value in enumerate(list):
        if value % 2 == 1:
            list[index] = 0
    return list   


def digitProduct(int):
    multiple = 1
    while int > 0:
        digit = int % 10
        multiple *= digit
        int = int // 10
    return multiple

def japanize(date):
    year = date[6:]
    day = date[3:5]
    month = date[:3]
    return year + "/" + month + day
        
def filereading(filename):
    counter = 0
    with open(filename, "r") as file:
        for lines in file.readlines()[1:]:
            line = lines.split(",")
            sprockets = int(line[2])
            counter += sprockets
    return counter

def alternatesum(list):
    total = 0
    for index, value in enumerate(list):
        if index % 2 == 1:
            list[index] = value*-1
    total = sum(list)
    return total

print(alternatesum([1,2,3,4,5]))
