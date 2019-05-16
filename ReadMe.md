#This is the ReadMe file of the game - Trump it
---------------------------------------------------
____________________________________________________________________________________________________
Made and Developed by: K@u5h!k46

#Current Version: 1.0.1

Version Details:

This is basic implementation of the game.
This doesn't have the betting option yet.
This version doesn't have input sanitisation.
Please help me find more bugs and any suggestion towards improving the code is highly appreciated.
_____________________________________________________________________________________________________

#How to Play:
-------------

-> This completely works on the principle of hierarchy.

-> The card deck consists of cards of all suits but from 9 to Ace in increasing order.

-> Firstly three cards at a time are distributed to all the players starting from the player on the right of the dealer. Call this play-wise.

-> Players look at their own cards and can declare the trump. 

-> First chance to declare the trump is given to the dealer and continues clock-wise till a trump is declared.

-> If no one's confident enough to declare the trump, the next set of cards are dealt in play-wise fashion.

-> Then again, trump is to be declared.

-> Now players start playing in the play-wise.

-> The person to play needs to drop a card. The suit he plays is "Base suit" for that round, and that suit must be maintained all the round unless:

	> A player doesn't have that suit. In which case he can either play a trump card called a "Cut" or play any other suit as his wish called "Widening".
	
	> A player wants to take a lead by "Cutting" the cards.
	
-> Cutting the cards doesn't change the base set for the round. Still the next player needs to play by the actual base set of the round.

-> The winner of the round is declared when all the players played a card in that respective round and decided by the hierarchy as below.


---->>>> Hierarchy in Trump > Hierarchy in the base set > Any other card.


Normal suit Hierarchy:
----------------------
Ace > King > Queen > Jack > 10 > 9

Trump Suit Hierarchy:
--------------------
Jack > 9 > Ace > King > Queen > 10


Each card has a value as shown in the table below.
-------------------------------------------------

*************************
* Card * Normal * Trump *
*************************
* Ace  *   11   *  11   *
*************************
* King *   03   *  03   *
*************************
* Queen*   02   *  02   *
*************************
* Jack *   01   *  20   *
*************************
*  10  *   10   *  10   *
*************************
*   9  *   00   *  14   *
*************************

-> The last round of the game gives out 5 additional points to the winner of that round.

-> Hence the total points per game are 146.

-> The trump declaring team requires 100 or more points to win.

-> The winner of the game is decided when the team that declared the trump crosses 100 points or when the other team crosses 46 points. In either case, the winning team makes sure that the other team cannot win.


#Support

Please help to improve this project either by 
1) Suggesting improvements to the Code
2) Reporting bugs 
3) Fixing Bugs
4) Joining the development team
