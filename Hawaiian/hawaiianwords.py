wdict = {
    "w" : ["w","v"]
}

voweldict = {
    "a" : "ah-",
    "e" : "eh-",
    "i" : "ee-",
    "o" : "oh-",
    "u" : "oo-"
}

consonantdict = {
    "p" : "p",
    "k" : "k",
    "h" : "h",
    "l" : "l",
    "m" : "m",
    "n" : "n",
    " " : " ",
    "'" : "'"
}

groupvoweldict = {
    "ai" : "eye-",
    "ae" : "eye-",
    "ao" : "ow-",
    "au" : "ow-",
    "ei" : "ay-",
    "eu" : "eh-oo-",
    "iu" : "ew-",
    "oi" : "oyo-",
    "ou" : "ow-",
    "ui" : "ooey-"
}


def main():
    string = check_input()
    word = pronounce(string)
    word = rmHyphen(word)
    print(word)
    valid = True
    while valid:
        question = input("Do you want to enter another word? Y/YES/N/NO ")
        if question.lower() not in ["yes", "y", "no", "n"]:
            print("Enter Y, YES, N, or NO")
            continue
        elif question.lower() == "y" or question.lower() == "yes":      # If yes, then does the steps again
            string = check_input()
            word = pronounce(string)
            word = rmHyphen(word)
            print(word)
        else:
            valid = False
            
    return word


def check_input():
    counter = 0
    valid = True
    while valid:
        word = input("Enter the word to pronounce: ")
        for char in word.lower():
            if char in ["a", "e", "i", "o", "u", "p", "k", "h", "l", "m", "n", "w", " ", "'"]:
                counter += 1
                if counter == len(word):
                    valid = False
            else:
                print(f"{char} is not a valid hawaiian character")
                valid = True
                counter = 0
    return word


def pronounce(string):
    result = ""
    index = 0
    while index < len(string):

        char = string[index].lower()

        if char in consonantdict:
            result += consonantdict[char]

        elif char in wdict:
            if char == "w" and string[index - 1] == "i" or string[index - 1] == "e":
                result += wdict[char][1]
            else:
                result += wdict[char][0]
        
        elif char in voweldict:
            if index != len(string) - 1 and char + string[index + 1] in groupvoweldict:     # looks at the char and the next char
                result += groupvoweldict[char + string[index + 1]]
                index += 1         # skips a char
            else:
                result += voweldict[char]

        index += 1
    return result.rstrip("-").capitalize()


# This function removes unwanted hyphens
# If there is a space or apostrophe in front of the hyphen, then it is removed
def rmHyphen(string):
    index = 0
    space = "- "
    apostrophe = "-'"
    while index < len(string) - 1:
        char = string[index]
        if char + string[index + 1] == space:
            string = string.replace(space, " ")
        elif char + string[index + 1] == apostrophe:
            string = string.replace(apostrophe, "'")
        index += 1
    return string


main()
