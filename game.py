from trump import *

points = [0, 0]

# winList[0] -> winner, winList[1] -> winnerCard, winList[2] -> roundPoints

winList = [None, None, 0]
gameWinner = None

origPlaywise = playwise


def check(ground, card):
    if (ground[0][1] == card[1]):
        return True
    else:
        return False


def pos(inputCard, shape):
    if shape == trump:
        for i in range(0, 6):
            if trumpSet[i][0] == inputCard[0]:
                return i
    else:
        for i in range(0, 6):
            if hierarchy[i][0] == inputCard[0]:
                return i


def decide(prevWinner, prevWinnerCard, playerNum, temp):

    if temp[1] == trump:
        for c in range(0, 6):
            if trumpSet[c][0] == temp[0]:
                winList[2] = winList[2] + trumpSet[c][1]
                #print((winList[2]))

    else:
        for c in range(0, 6):
            if hierarchy[c][0] == temp[0]:
                winList[2] = winList[2] + hierarchy[c][1]
                #print(int(winList[2]))

    if prevWinner == None:
        return playerNum

    elif temp[1] != trump and temp[1] != ground[0][1]:
        return prevWinner
    elif prevWinnerCard[1] == trump and temp[1] != trump:
        return prevWinner
    elif prevWinnerCard[1] != trump and temp[1] == trump:
        return playerNum
    elif prevWinnerCard[1] == trump and temp[1] == trump:
        if pos(prevWinnerCard, trump) < pos(temp, trump):
            return prevWinner
        else:
            return playerNum
    elif prevWinnerCard[1] != trump and temp[1] != trump:
        if pos(prevWinnerCard, ground[0][1]) < pos(temp, ground[0][1]):
            return prevWinner
        else:
            return playerNum

def popCard(player):
    player_cards(player, 2*numOfCards, 0)
    popIndex = int(input("\nEnter the card number to drop: ")) - 1
    temp = player[3].pop(popIndex)
    ground.append(temp)
    result = decide(winList[0], winList[1], player[1], temp)
    if result == player[1]:
        winList[1] = temp

    return result



for i in range(0, 2*numOfCards):
    ground.clear()

    for player in playwise:

        os.system("clear")
        print("TEAMS:\n")
        print("Team1:")
        for p in team0:
            print(p[0])
        print()
        print("Team2:")
        for p in team1:
            print(p[0])
        print()
        print("Trump is declared by " + str(trumpPlayer))
        print("Trump is " + trump + "\n")
        print("Current points are:\nTeam1: " + str(points[0]) + "\nTeam2: " + str(points[1]) + "\n")

        print("Cards on the ground are:")

        for card in ground:
            print(card)
        # print()

        print("points on the ground are: " + str(winList[2]) + "\n")

        ans = popCard(player)
        winList[0] = ans
        print(winList[0])

    temp = origPlaywise[winList[0]:]
    temp.extend(origPlaywise[:winList[0]])
    playwise = temp

    points[winList[0] % 2] = winList[2] + points[winList[0] % 2]
    if i == (2 * numOfCards - 1):
        points[winList[0] % 2] += 5
    winList[2] = 0
    winList[0] = None
    winList[1] = None

    if points[trumpTeam] >= 100:
        gameWinner = str(trumpTeam+1)
        break
    elif points[nonTrumpTeam] >= 47:
        gameWinner = str(nonTrumpTeam+1)
        break


print("\nGame Over!\n")
print("The winner is Team" + str(gameWinner))