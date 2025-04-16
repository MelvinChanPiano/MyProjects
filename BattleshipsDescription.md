1-player Battleships game (text-based)
Programming language: Python

Purpose of Code:
To imitate the battleships game using text input. The player can set up and
position the pieces while the bot position its pieces randomly.
The player can get to start first or not.
Each attack reveals if it hits a ship or not by ‘x’ or ‘o’.
The bot will attack randomly.
A message will appear to indicate whether

Scale of project: 
370 lines (excluding spaces), number of classes: 7.
Number of functions (outside classes) : 16

OOP concepts:
The 5 different ships inherit the class ships:(super.__init__() )
Encapsulation is used with attributes and methods, for example, self.length is
decreased by 1 when hit(self) is called. Composition is used that the Player
class contains the an instance of the Board class.

Interesting implementations:
3 boards are used, but only 2 are displayed. The
AI display board (Fboard, for players to view) needs to map the board of the
actual AI board when the player chooses a coordinate to hit.
A string grid is used to represent the board, so each coordinate is encoded.
