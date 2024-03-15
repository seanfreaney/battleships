import random

class Board: 
    """
    Class to set board size and display.
    """
    def __init__(self, size, num_ships):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)] #Project 3 scope video
        self.num_ships = num_ships
        self.ships = [] #initialise ships list
        self.place_ships_randomly(num_ships)
    
    def print(self):
        for row in self.board:
            print(" ".join(row))

    def place_ships_randomly(self, num_ships):
        row = random.randint(0, self.size - 1)
        col = random.randint(0, self.size - 1)
        self.board[row][col] = "X"
        self.ships.append((row, col))


class Player:
    """
    Class to represent player.
    """
    def __init__(self, name, size, num_ships):
        self.name = name
        self.board = Board(size, num_ships)


def game():
    size = 6
    num_ships = 5
    
    player_board = Board(size, num_ships)
    computer_board = Board(size, num_ships)

    player1 = Player("Sean", size, num_ships)
    computer = Player("Computer", size, num_ships)

    #Project 3 Scope video
    print("Welcome to Battleships")
    print(f"Board Size: {size} * {size}.")
    #placeholder for num ships message
    print("Top left corner is row: 0, column: 0")
    print("-" * 35)

    print("\nComputer Board:")
    computer_board.print()

    print("\nPlayer Board:")
    player_board.print()

game()

   
    
