*Tic Tac Toe Game*
A simple implementation of the classic Tic Tac Toe game in Python.

**Game Description**
The game is played on a 3x3 grid, with two players, X and O, taking turns to mark a square. 
The first player to get three in a row (horizontally, vertically, or diagonally) wins the game. If all squares are filled and no player has won, the game is a draw.

**Features**
Simple and intuitive gameplay
Clear and concise game board display
Input validation to ensure players enter valid moves
Automatic game reset after each game

**Code Structure**
The code is organized into the following sections:

check_win function: checks if a player has won the game
tic_tac_toe function: implements the game logic
game_table and tic_table variables: store the game board state
Main game loop: runs the game repeatedly until the player chooses to quit

**Requirements**
* Python 3.x
* prettytable library (for game board display)
**Usage**
Run the game by executing the Python script.
Follow the prompts to play the game.
Enter your moves by typing the number of the square where you want to play.
The game will prompt for reset after each game.
To quit the game, enter 'n' , or any character really, when prompted to play again.
