def main():
    string = check_input()

    wdict = {
        "w" : ["w","v"]
    }

    voweldict = {
        "a" : "ah",
        "e" : "eh",
        "i" : "ee",
        "o" : "oh",
        "u" : "oo"
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
        "ai" : "eye",
        "ae" : "eye",
        "ao" : "ow",
        "au" : "ow",
        "ei" : "ay",
        "eu" : "eh-oo",
        "iu" : "ew",
        "oi" : "oyo",
        "ou" : "ow",
        "ui" : "ooey"
    }

    groupvalue = ""

    for index, char in enumerate(string):
        if char in consonantdict:
            print(consonantdict[char], end="")

        #elif char in groupvoweldict:    #buggy
        


        elif char in voweldict:
            if index != len(string) - 1:
                print(voweldict[char] + "-",end="")
            else:
                print(voweldict[char], end="")

        elif char in wdict:
            if char == "w" and string[index - 1] == "i" or string[index - 1] == "e":   #buggy
                print(wdict[char][1], end="")
            else:
                print(wdict[char][0], end="")

    
    




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
    return word

main()
