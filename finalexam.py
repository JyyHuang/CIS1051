import random

def sumOfPositive(lists):
    arr = []
    for list in lists:
        for nums in list:
            if nums >= 0:
                arr.append(nums)
    return sum(arr)



def whoWonWhy(filename):
    highest_score = 0
    highest_score_name = ""
    with open(filename,"r") as file:
        for lines in file.readlines():
            line = lines.split(",")
            name = line[0]
            score = line[1]
            if int(score) > int(highest_score):
                highest_score = score
                highest_score_name = name
        print(f"{highest_score_name} won with score of {highest_score}")



def roll():
    return random.choice(["Red", "Green","Blue","Yellow","Basket","Raven"])

def firstOrchard():
    dict = {
        "red":4,
        "green":4,
        "blue":4,
        "yellow":4
    }
    Ravencounter = 0
    counter = 0
    done = False
    while not done:
        turn = roll()
        if turn == "Red":
            if dict["red"] != 0:
                dict["red"] -= 1
        elif turn == "Green":
            if dict["green"] != 0:
                dict["green"] -= 1
        elif turn == "Blue":
            if dict["blue"] != 0:
                dict["blue"] -= 1
        elif turn == "Yellow":
            if dict["yellow"] != 0:
                dict["yellow"] -= 1
        elif turn == "Basket":
            highest_remaining = 0
            highest_remaining_name = ""
            for i in dict.keys():
                if dict[i] > highest_remaining:
                    highest_remaining = dict[i]
                    highest_remaining_name = i
            if dict[highest_remaining_name] != 0:
                dict[highest_remaining_name] -= 1
        else:
            Ravencounter += 1

        counter += 1

        if dict["red"] == 0 and dict["green"] == 0 and dict["blue"] == 0 and dict["yellow"] == 0:
            done = True
        elif Ravencounter == 5:
            done = True
    return counter


def simulation():
    TRIALS = 100000
    total_turns = 0
    for i in range(TRIALS):
        total_turns += firstOrchard()
    return total_turns/TRIALS



