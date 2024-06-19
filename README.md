# Scrabble Game in Python
This is a Python implementation of the classic board game Scrabble. The game allows multiple players (including a computer player) to take turns forming words on a virtual board using letter tiles.

# Table of Contents
* Features
* Requirements
* Setup Instructions
* Gameplay Instructions
* Code Structure
* Contributing
  
# Features
* Players: Supports a human player and one computer player.
* Scoring: Calculates scores based on letter points and word multipliers on the board.
* Tile Management: Players can draw tiles from a bag and refill their racks.
* Board Interactions: Words can be placed horizontally or vertically on the board, taking advantage of score multipliers.
# Requirements
* Python  environment
* Standard Python libraries (random, collections)
# Setup Instructions
1. Clone the repository:

```bash
git clone https://github.com/Joy-Mbuvi/SCRABBLE-GAME-.git

```
2. Ensure you have Python environment installed. You can download it from [python.org](https://www.python.org/downloads/) 

3. Run the game:

```bash
python3 scrabble.py
```
# Gameplay Instructions
* Follow the prompts to enter your name.
* Each player takes turns to form words using their letter tiles.
* You can enter a word to play, or type 'SHUFFLE' to shuffle your rack.
* Specify the starting position (row and column) and direction (right or down) for placing the word on the board.
* The game ends when all words in the dictionary have been played or players decide to end it.
# Code Structure
The main components of the code include:

* scrabble.py: The main Python script that implements the game logic.
* Tile, Tile_bag, Player, ComputerPlayer: Classes defining tiles, the tile bag, player actions, and computer player behavior.
* Board, Word: Classes managing the game board and words played on it.

# Contributing
Contributions are welcome! If you have any suggestions or find a bug, please open an issue or submit a pull request.





