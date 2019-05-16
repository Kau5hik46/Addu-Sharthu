import os
from lobby import *

ground = []

def player_cards(player, cardNum, clear):

    if int(clear) == 1:
        os.system("clear")

    print("Player Name: " + player[0])
    input("Press return/enter to show the cards: ")
    a = None
    if cardNum > len(player[3]):
        a = len(player[3])
    else:
        a = cardNum
    for i in range(0, a):
        print(player[3][i])

    print()


def joint(player, numOfCards):
    print("Choose the cards to put the joint: ")

    if numOfCards == 2:
        ground.extend(player[3][0:numOfCards])

    else:
        i = None
        for i in range(0, numOfCards):
            result = input("Do you want to pop card " + str(player[3][i]) + "?: ")
            if result == "yes" or result == "Yes":
                ground.append(player[3][i])
            else:
                i += 1
                ground.extend(player[3][i:numOfCards])
                break


    os.system("clear")
    print("Joint of: ")
    for card in ground:
        print(str(card))

    print()

    player_cards(player, 2*numOfCards, 0)
    return declare(player, 1, numOfCards)


def aakhar(player):
    return (player[3][2*numOfCards - 1][1], player[2])


def declare(player, number, numOfCards):
    if number == 1:
        shapes = ["Spades", "Diamonds", "Clovers", "Hearts"]
        result = int(input("Trump is:\n1)Spades\n2)Diamonds\n3)Clovers\n4)Hearts\nChoose the option: "))
        return (shapes[result - 1], player[2])
    elif number == 2:
        return joint(player, numOfCards)
    elif number == 3:
        return aakhar(player)


def prompt(player, numOfCards):
    result = input("Do you want to declare the trump?\nType 1 for Yes and 0 for No: ")
    if int(result) == 1:
        trumpType = int(input("How do you want to declare trump?\n1) Normal\n2) Joint\n3) Aakhar\nType option number: "))
        print()
        return declare(player, trumpType, numOfCards)
    else:
        return "pass"


trump = None
trumpTeam = None
trumpPlayer = None

for player in antiplaywise:
    player_cards(player, numOfCards, 1)
    ans = prompt(player, numOfCards)
    if ans == "pass":
        continue
    else:
        trump = ans[0]
        trumpTeam = ans[1]
        trumpPlayer = player[0]
        break

if trump == None:
    for player in antiplaywise:
        player_cards(player, 2*numOfCards, 1)
        ans = prompt(player, 2*numOfCards)
        if ans == "pass":
            continue
        else:
            trump = ans[0]
            trumpTeam = ans[1]
            trumpPlayer = player[0]
            break

if trump == None:
    print("No trump is declared!")
    exit(-3)

nonTrumpTeam = None
if trumpTeam == 0:
    nonTrumpTeam = 1
else:
    nonTrumpTeam = 0

