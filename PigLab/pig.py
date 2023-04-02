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
    turns = 0
    while turn_total + score <= 100:
        roll = random.randint(1, 6)
        print(f"Roll: {roll}")
        if roll == 1:
            turn_total = 0
            print(f"Turn total: {turn_total}")
            print(f"New Score: {score}")
            turns += 1
        else:
            turn_total += roll
            if turn_total >= 20:
                score += turn_total
                print(f"Turn total: {turn_total}")
                print(f"New Score: {score}")
                turn_total = 0
                turns += 1
            elif turn_total + score >= 100:
                score += turn_total
                print(f"Turn total: {turn_total}")
                print(f"New Score: {score}")
                turns += 1
    return turns


def averageturns(games):
    arr = []
    for i in range(games):
        x = holdat20orGoalGame()
        arr.append(x)
    average = sum(arr) / games
    print(f"Average turns: {average}")
    return average


def twoPlayerPig():
    player1 = True
    player2 = False
    p1score = 0
    p2score = 0
    valid = True
    while valid:
        print(f"Player 1 score: {p1score}")
        print(f"Player 2 score: {p2score}")
        if player1 == True:
            print("It is player 1's turn.")
            x = holdAt20orGoal(p1score)
            player1 = False
            player2 = True
            if x != 0:
                p1score = x
        elif player2 == True:
            print("It is player 2's turn.")
            y = holdAt20orGoal(p2score)
            player1 = True
            player2 = False
            if y != 0:
                p2score = y
        if p1score >= 100 or p2score >= 100:
            print(f"Player 1 score: {p1score}")
            print(f"Player 2 score: {p2score}")
            break


def pig():
    number = random.randint(1, 2)
    print(f"You will be player {number}.")
    print("Enter nothing to roll; enter anything to hold.")
    print("It is player 1's turn.")
    p1score = 0
    p2score = 0
    turn_total = 0
    player1 = True
    player2 = False
    valid = True
    while True:
        # if the number is one, it goes to the person first, and then the ai
        if number == 1:
            if player1 == True:
                print(f"Player 1 score: {p1score}")
                print(f"Player 2 score: {p2score}")
                while valid:
                    roll = random.randint(1, 6)
                    print(f"Roll: {roll}")
                    if roll == 1:
                        turn_total = 0
                        valid = False
                    else:
                        turn_total += roll
                        user = input(f"Turn total: {turn_total} Roll/Hold?")
                        if len(user) == 0:
                            valid = True
                        else:
                            valid = False
                p1score += turn_total
                turn_total = 0
                turn = 2
                if p1score >= 100 or p2score >= 100:
                    print(f"Player 1 score: {p1score}")
                    print(f"Player 2 score: {p2score}")
                    break
                print(f"It is player {turn}'s turn.")
                player1 = False
                player2 = True
            elif player2 == True:
                print(f"Player 1 score: {p1score}")
                print(f"Player 2 score: {p2score}")
                x = holdAt20orGoal(p2score)
                turn = 1
                if x != 0:
                    p2score = x
                if p1score >= 100 or p2score >= 100:
                    print(f"Player 1 score: {p1score}")
                    print(f"Player 2 score: {p2score}")
                    break
                print(f"It is player {turn}'s turn.")
                player1 = True
                player2 = False
                valid = True
        # if the number is two, it goes to the ai first, and then the person
        else:
            if player1 == True:
                print(f"Player 1 score: {p1score}")
                print(f"Player 2 score: {p2score}")
                x = holdAt20orGoal(p1score)
                turn = 2
                if x != 0:
                    p1score = x
                if p1score >= 100 or p2score >= 100:
                    print(f"Player 1 score: {p1score}")
                    print(f"Player 2 score: {p2score}")
                    break
                print(f"It is player {turn}'s turn.")
                player1 = False
                player2 = True
                valid = True
            elif player2 == True:
                print(f"Player 1 score: {p1score}")
                print(f"Player 2 score: {p2score}")
                while valid:
                    roll = random.randint(1, 6)
                    print(f"Roll: {roll}")
                    if roll == 1:
                        turn_total = 0
                        valid = False
                    else:
                        turn_total += roll
                        user = input(f"Turn total: {turn_total} Roll/Hold?")
                        if len(user) == 0:
                            valid = True
                        else:
                            valid = False
                p2score += turn_total
                turn_total = 0
                turn = 1
                if p1score >= 100 or p2score >= 100:
                    print(f"Player 1 score: {p1score}")
                    print(f"Player 2 score: {p2score}")
                    break
                print(f"It is player {turn}'s turn.")
                player1 = True
                player2 = False
        



#turn()
#holdAt20Outcomes(10000)
#turn()
#holdAtXOutcomes(10000, 100)
#holdAt20orGoal(0)
#holdat20orGoalGame()
#averageturns(10000)
#twoPlayerPig()
#pig()