import random

class Board: 
    """
    Class to set board size and display board.
    """
    def __init__(self, size, num_ships):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)] #Project 3 scope video
        self.num_ships = num_ships
        self.ships = [] #initialise ships list
    
    def print(self): #Project 3 scope video
        for row in self.board:
            print(" ".join(row))

    def hide_ship(self):
        hidden_board = [row[:] for row in self.board] #create new list (to be used for making guesses) by iterating over each row of the existing board

        # Hide the ships
        for row, col in self.ships: #loop over each ship
            hidden_board[row][col] = "." #hide X with .
        return hidden_board
    
    def make_guess(self, row, col):
        if self.board[row][col] == "X":
            print("Hit!")
            self.board[row][col] = "@"
            return True
        else:
            print("Miss!")
            self.board[row][col] = "0"
            return False

class Player:
    """
    Class to represent player.
    """
    def __init__(self, name, size, num_ships):
        self.name = name
        self.board = Board(size, num_ships)


def populate_board(board_obj, num_ships):
    """
    Function to populate board.
    """
    size = board_obj.size #access size attribute of board object
    ships_on_board = 0 #initialise ships_on_board variable to count ships populated

    while ships_on_board < num_ships: #loop that will run while ships_on_board is less than num_ships
        row = random.randint(0, size - 1) #generate random row & col points within board range
        col = random.randint(0, size - 1)
        if board_obj.board[row][col] == ".": #check if random points are empty
            board_obj.board[row][col] = 'X' #if empty place a ship there
            board_obj.ships.append((row,col)) #append coordinates to ships list
            ships_on_board += 1 #increment ships on board by one


def validate_coordinates(size):
    try:
        
        guess_row = int(input("Enter the row number to guess (0 to {}): ".format(size - 1)))
        guess_col = int(input("Enter the column number to guess (0 to {}): ".format(size - 1)))
        
        if 0 <= guess_row < size and 0 <= guess_col < size:
            return guess_row, guess_col
        else:
            print("Please enter valid row and column numbers.")
            return validate_coordinates(size)
    except ValueError:
        print("Please enter valid integers for row and column.")
        return validate_coordinates(size)


def game_loop(player_board, computer_board, size):
    
    while True:

        guess_row, guess_col = validate_coordinates(size)
    
    # Player makes a guess on the hidden computer board
        is_hit = computer_board.make_guess(guess_row, guess_col)
        
        # Display the hidden computer board with player's guess
        hidden_computer_board = computer_board.hide_ship()
        print("\nComputer's Hidden Board:")
        for row in hidden_computer_board:
            print(" ".join(row))
        
        # Check if all ships are sunk
        if all(cell != "X" for row in computer_board.board for cell in row):
            print("Congratulations! You have sunk all computer's ships!")
            break



def game():
    size = 3
    num_ships = 2

    player_board = Board(size, num_ships)
    computer_board = Board(size, num_ships)

    # Populate both player's and computer's boards
    populate_board(player_board, num_ships)
    populate_board(computer_board, num_ships)

    # Hide ships on computer's board
    hidden_computer_board = computer_board.hide_ship()

    #Project 3 Scope video
    print("Welcome to Battleships")
    print(f"Board Size: {size} * {size}.")
    #placeholder for num ships message
    print("Top left corner is row: 0, column: 0")
    player_name = input("Enter your name: ")
    print("-" * 35)
    
    print(f"{player_name}'s Board: ")
    player_board.print()

    print("\nComputer's Hidden Board:")
    for row in hidden_computer_board:
        print(" ".join(row))
    
    game_loop(player_board, computer_board, size)
    
    

game()

   
    
