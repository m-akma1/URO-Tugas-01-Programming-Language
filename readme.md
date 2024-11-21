# The Battle of Robots
The Battle of Robots is a combat strategy game with two game modes: PvP or PvC. The main objective of this game is to win a fight against other team. Each team consist of 4 different robots. The game runs in CLI Terminal with minimal UI. 

## Main Features
* **2 Game Modes**: Users can choose from two types of modes: Player vs Player (PvP) or Play Against Computer.
* **10 Unique Robots**: The robots named after Greek letters with varying power and health stats. For detailed information, see [robots](robots.md).
* **Robot Battles**: Each game consists of a battle, where the leading robots from each team duel until one or both are killed.
* **Random Selection (for Computer)**: When playing against the Computer, the teams selected are drawn at random, creating variations in the results.

## How to Play
Run the program `main.py` with any Python interpreter. Before playing, the program will ask which game mode to choose.

### PvP Mode
* First player writes their name then chooses 4 different robots from the 10 robots provided.
* Robot selection is done by entering the selected index into the terminal.
* The program shows the first player's team, then the second player initiates similarly.
* The battle runs automatically, players only need to see the battle progress on the terminal.

### PvC Mode
* The player initialization similar to PvP.
* Player's initialization, the program will initiate the Computer's team randomly.
* Battles run similar to PvP mode.

### Gameplay and Winner
* When each battle begins, each team's most-front robots will duel and attack simultaneously.
* The attack and health points of each robot will be shown for each attack.
* When any robots run out of health, the battle is over and any destroyed robots will be removed from the team.
* A new battle continues until any players have no robots left.
* When a player has no robots left, the other player wins.
* If both players run out of robots at the same time, the game ends in a draw.

## Game Info
### Version 0.1
Language: Python 3.13  
Finished Developing: 8 October 2024  
Release Date: 21 November 2024  

### Key Updates
* Added 10 robots with basic health and power
* Added PvP and PvC gamemode
* Added basic delay animation
* Finished basic game logic and structure
