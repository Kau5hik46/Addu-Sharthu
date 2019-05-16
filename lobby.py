from player_info import *

hierarchy = [('A', 11), ('K', 3), ('Q', 2), ('J', 1), (10, 10), (9, 0)]
trumpSet = [('J', 20), (9, 14), ('A', 11), ('K', 3), ('Q', 2), (10, 10)]


playwise = []

for i in range(0, num_of_players):
    if i % 2 == 0:
        playwise.append(team0[int(i/2)])
    else:
        playwise.append(team1[int(i/2)])



antiplaywise = playwise[::-1]
print(antiplaywise)




