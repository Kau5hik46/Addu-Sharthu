import random

#import player_info

shapes = ["Spades", "Diamonds", "Clovers", "Hearts"]
numbers = ["A", 9, 10, "J", "Q", "K"]

deck = []

for shape in shapes:
    for number in numbers:
        deck.append((number, shape))

random.shuffle(deck)
