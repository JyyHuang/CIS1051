import random
def turn():
    turn_total = 0
    while True:
        oneroll = roll()
        #print(f"Roll: {oneroll}")
        if oneroll == 1:
            turn_total = 0
            break
        else:
            turn_total += oneroll
            if turn_total >= 20:
                break
    #print(f"Turn total: {turn_total}")
    return turn_total

def roll():
    roll = random.randint(1, 6)
    return roll


def simulation(trials):
    dict = {0:0}
    for val in range(20, 26):
        dict[val] = 0
    for i in range(trials):
        score = turn()
        dict[score] += 1

    print("Score\tEstimated Probability")
    for i in dict:
        dict[i] = dict[i] / trials
        print("{}\t{:.6f}".format(i,dict[i]))

def holdAtX(trials, X):
    pass

simulation(10000)
