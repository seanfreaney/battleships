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


def game():

    size = 5
    board = Board(size)
    board.print()

game()

   
    
