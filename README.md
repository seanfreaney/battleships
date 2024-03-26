# Battleships

Battleships is a pyton terminal game shich runs in the Code Institue mock terminal on Heroku.
Users play against a computer to try and guess the location of the computer's ships before the computer finds theirs.
The board is 4 * 4 squares and contains 3 ships, each ships occupies 1 square
- the live link can be found here: <https://battlesean-e791976cdc64.herokuapp.com/>

## How to Play
In this version of the classic game, the player enetrs their name and two boards are randomly generated.
The player's name is displayed over their board and their ships are visible ('X'). The ships on the computer board remain invisible.
The player can then enter row and column coordinates to guess the location of the computer's ships.
The computer then guesses the coordinates of the player's ships.
The player can quit during the game or the game will end once either the player or the computer ships have been sunk.
The player is then asked of they would like to replay.

## Existing Features
- User inputs their name,
- Computer and Player boards are randomly generated,
- Computer board is invisible, Player board is visible.
![name input, board generation](assets/images/setup.png)
- Input validation:
  - guesses outside of range
  - invalid input
- Computer guesses on player board
![validate coordinates, outside range and letters](assets/images/validate%20coordinates%20-%20too%20big,%20letters.png)
- Input validation: 
  - can't guess same square twice
![validate coordinates, same coordinates](assets/images/validate%20coordinates,%20same%20coordinates.png)
- Ability to quit game before game ending
![ability to quit during game](assets/images/ability%20to%20quit%20mid%20game.png)
- Ability to replay game when all ships sunk
![option to replay when ships sunk](assets/images/replay%20game%20ships%20sunk.png)

## Future Features
- Ability to have multiple players
- Ability to set the board size
- Ability to select number of ships
- Ability to select ship locations

## Testing
I have manually tested the project in the following ways:
- Passed code through PEP8 CI Linter with no errors
- Given invalid inputs: outside of range, strings and same input twice
- Tested in local terminal and and CI Heroku terminal

## Validator Testing
- PEP8 CI Python Linter
  - no errors returned, however, multiple lines too long but I couldn't change this as it affected the syntax of code.

## Deployment
- Steps for deployment
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildpacks to Python and NodeJS in that order
  - Link the Heroku app to the repository
  - Click on Deploy

## Credits
 - Code Institue for deployment terminal
 - Code Institute Project 3 scope video
 - if not: <https://www.geeksforgeeks.org/python-if-with-not-operator/>
 - if in: <https://www.w3schools.com/python/gloss_python_check_if_set_item_exists.asp>
