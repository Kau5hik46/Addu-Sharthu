from os import system

print("Welcome to Addu-Sharthu Lobby: \n")

print("1) Play the Game")
print("2) How to play?")
print("3) Version info and Support")
print("4) Quit the lobby")

choice  = int(input("Please choose a suitable option: "))

if choice == 4:
    print("Bye!")
    exit(0x12345678)

elif choice == 2:
    howToPlay = open("sources/htp.txt", "r")

    for word in howToPlay:
        print(word, end='')

    howToPlay.close()
    input("Press any key to continue: ")
    system("clear")

    from menu.py import *

elif choice == 3:
    credit = open("sources/credits.txt", "r")

    for word in credit:
        print(word, end='')
    credit.close()
    input("Press any key to continue: ")
    system("clear")

    from menu.py import *

elif choice == 1:
    from game.py import *

    #from menu.py import *

else:
    print("Please choose an proper option!")
    from menu.py import *


