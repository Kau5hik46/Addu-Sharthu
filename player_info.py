# Collects information of players and divides teams.

# Players class

from card_deck import *



class player:

    def __init__(self):
        self.position = None
        self.name = str(input("Enter the player name: "))
        self.team = None
        self.cards = []

    def place(self, pos):
        self.position = int(pos)
        self.team = self.position % 2

    def add_cards(self, deck, numOfCards):
        for i in range(0, numOfCards):
            self.cards.append(deck.pop(0))

        for i in range(0, numOfCards):
            self.cards.append(deck.pop(0))

num_of_players = None

while True:
    num_of_players = int(input("Enter the number of players: "))
    if num_of_players != 4 and num_of_players != 6:
        print("Invalid player number! Retry")
        continue
    else:
        break

numOfCards = int((24/int(num_of_players))/2)

team0 = []
team1 = []

for i in range(0, num_of_players):
    if i % 2 == 0:
        p = player()
        p.place(i)
        p.add_cards(deck, numOfCards)
        team0.append((p.name, p.position, p.team, p.cards))

    else:
        p = player()
        p.place(i)
        p.add_cards(deck, numOfCards)
        team1.append((p.name, p.position, p.team, p.cards))

