import random

class Board: 
    """
    Class to set board size and display.
    """
    def __init__(self, size):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)] #Project 3 logic/scope video
    
    def print(self):
        for row in self.board:
            print(" ".join(row))


class Player:
    """
    Class to represent player.
    """
    def __init__(self, name, size):
        self.name = name
        self.board = Board(size)


def game():
    size = 6
    player_board = Board(size)
    computer_board = Board(size)

    player = Player("Sean", size)

    print("Player Board:")
    player_board.print()

    print("\nComputer Board:")
    computer_board.print()

game()

   
    
