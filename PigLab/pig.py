import random
def turn(limit=20):
    turn_total = 0
    while True:
        roll = random.randint(1, 6)
        #print(f"Roll: {roll}")
        if roll == 1:
            turn_total = 0
            break
        else:
            turn_total += roll
            if turn_total >= limit:
                break
    #print(f"Turn total: {turn_total}")
    return turn_total


def holdAt20Outcomes(trials):
    dict = {0:0}
    for val in range(20, 26):
        dict[val] = 0
    for i in range(trials):
        score = turn()
        dict[score] += 1
    print("Score\tEstimated Probability")
    for i in dict:
        dict[i] = dict[i] / trials
        print("{}\t{:.6f}".format(i, dict[i]))


def holdAtXOutcomes(trials, limit):
    dict = {0:0}
    for val in range(limit, limit + 6):
        dict[val] = 0
    for i in range(trials):
        score = turn(limit)
        dict[score] += 1
    print("Score\tEstimated Probability")
    for i in dict:
        dict[i] = dict[i] / trials
        print("{}\t{:.6f}".format(i, dict[i]))


def holdAt20orGoal(score, limit=20):
    turn_total = 0
    while True:
        roll = random.randint(1, 6)
        print(f"Roll: {roll}")
        if roll == 1:
            turn_total = 0
            break
        else:
            turn_total += roll
            if turn_total >= limit:
                break
            elif turn_total + score >= 100:
                break
    score += turn_total

    print(f"Turn total: {turn_total}")
    print(f"New Score: {score}")
    return score

def holdat20orGoalGame():
    score = 0
    turn_total = 0
    while turn_total + score <= 100:
        roll = random.randint(1, 6)
        print(f"Roll: {roll}")
        if roll == 1:
            turn_total = 0
            print(f"Turn total: {turn_total}")
            print(f"New Score: {score}")
        else:
            turn_total += roll
            if turn_total >= 20:
                score += turn_total
                print(f"Turn total: {turn_total}")
                print(f"New Score: {score}")
                turn_total = 0
    return score

#holdAt20Outcomes(10000)
#turn()
#holdAtXOutcomes(10000, 100)
#holdAt20orGoal(90)
holdat20orGoalGame()