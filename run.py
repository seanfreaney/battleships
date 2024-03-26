import random


class Board:
    """
    Class to set board size and display board.
    """

    def __init__(self, size, num_ships):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]  # Project 3 scope video
        self.num_ships = num_ships
        self.ships = []  # initialise ships list

    def print(self):  # Project 3 scope video
        """
        Method to print the board.
        """

        for row in self.board:
            print(" ".join(row))

    def hide_ship(self):
        """
        Method to hide ships on the board.
        """

        # Create new list (to be used for making guesses) by iterating over each row of the existing board
        hidden_board = [row[:] for row in self.board]

        # Hide the ships
        for row, col in self.ships:  # loop over each ship
            if self.board[row][col] == "@":
                hidden_board[row][col] = "@"  # if the ships is hit show an @
            else:
                hidden_board[row][col] = "."  # otherwise keep hidden with .

        return hidden_board

    def make_guess(self, row, col):
        """
        Method to make a guess on the board.
        """
        # Check if guessed position contains an X
        if self.board[row][col] == "X":
            # If the guess hits a ship, mark it as a hit
            self.board[row][col] = "@"
            return True  # Return True to indicate a hit
        else:
            # If the guess misses the ship, mark it as a miss
            self.board[row][col] = "0"
            return False # Return False to indicate a miss

    def random_guess(self, guessed_positions):  # Project 3 Scope video
        """
        Method to make a random guess on the board.

        """

        while True:
            # Generate random row and column indices within the size of the board
            row = random.randint(0, self.size - 1)  # Generate a random row within range
            col = random.randint(0, self.size - 1)  # Generate a random col within range
            # Check if the randomly generated position has not been guessed before
            if (row, col) not in guessed_positions:
                return row, col


def populate_board(board_obj, num_ships):
    """
    Function to populate board.
    """

    size = board_obj.size  # access size attribute of board object
    ships_on_board = 0  # initialise ships_on_board variable to count ships populated

    while ships_on_board < num_ships:  # loop that will run while ships_on_board is less than num_ships
        row = random.randint(0, size - 1)  # generate random row & col points within board range
        col = random.randint(0, size - 1)
        if board_obj.board[row][col] == ".":  # check if random points are empty
            board_obj.board[row][col] = 'X'  # if empty place a ship there
            board_obj.ships.append((row, col))  # append coordinates to ships list
            ships_on_board += 1  # increment ships on board by one


def validate_coordinates(size, guessed_positions):
    """
    Function to validate player's guesses.
    """

    try:  # try-except block to handle invalid input. If guesses not integers function calls itself again
        guess_row = int(input("Enter the row number to guess (0 to {}): \n".format(size - 1)))
        guess_col = int(input("Enter the column number to guess (0 to {}): \n".format(size - 1)))

        # check if player's guesses are not within the board range. If true, print message and call function recursively
        if not (0 <= guess_row < size and 0 <= guess_col < size):  # Geeks for geeks if with not operator
            print("Please enter valid row and column numbers.")
            return validate_coordinates(size, guessed_positions)

        # Check if player's guesses have already been guessed. If true, print message and call function recursively
        if (guess_row, guess_col) in guessed_positions:  # w3schools python check if set item exists
            print("You've already guessed this position. Please try again.")
            return validate_coordinates(size, guessed_positions)

        guessed_positions.add((guess_row, guess_col))  # Add the guessed position to the set
        return guess_row, guess_col

    except ValueError:
        print("Please enter valid integers for row and column.")
        return validate_coordinates(size, guessed_positions)


def game_loop(player_board, computer_board, size, player_name):
    """
    Function to run the game loop.

    Manages the turns between the player and computer, allowing each to make guesses
    on the opponent's board until one player sinks all of the opponent's ships or
    the player decides to quit.
    """

    guessed_positions_player = set()  # initialise an empty set to store player guesses
    guessed_positions_computer = set()  # initialise an empty set to store computer guesses

    while True:

        # Allow player to quit game during each iteration of game loop
        quit_game = input("Enter 'q' to quit the game, or press any key to continue: \n")
        if quit_game.lower() == 'q':
            # print("Quitting the game...")
            return "quit"  # Return "quit" to indicate the player wants to quit the game

        # Player's turn

        # Get validated coordinates using validate_coordinates function
        guess_row, guess_col = validate_coordinates(size, guessed_positions_player)

        # Call makes_guess method of computer_board object passing player's guess_row and guess_col parameters
        is_hit = computer_board.make_guess(guess_row, guess_col)

        # Print result of player's guess
        if is_hit:
            print("\nHit!")
        else:
            print("\nMiss!")

        # Display the hidden computer board with player's guess
        hidden_computer_board = computer_board.hide_ship()
        print("\nComputer's Board:")
        for row in hidden_computer_board:
            print(" ".join(row))

        # Check if all ships are sunk
        if all(cell != "X" for row in computer_board.board for cell in row):
            print("Congratulations! You have sunk all computer's ships!")
            return "game_over"  # Return "game_over" to indicate the game is over

        # Computer's turn

        # Call random_guess method of player_board object passing the set 'guessed_positions_computer'.
        # Returning a tuple with random coordinates which ahve not yet been used
        computer_guess_row, computer_guess_col = player_board.random_guess(guessed_positions_computer)

        # Call makes_guess method of computer_board object passing random coordinates (generated above)
        is_hit = player_board.make_guess(computer_guess_row, computer_guess_col)

        # Add computer's guess to guessed_positions_computer set
        guessed_positions_computer.add((computer_guess_row, computer_guess_col))
        print("\nComputer guessed row:", computer_guess_row, "col:", computer_guess_col)

        # Print result of Computer's guess
        if is_hit:
            print("\nHit!")
        else:
            print("\nMiss!")

        print(f"\n{player_name}'s Board:")
        player_board.print()
        print()  # Add an empty line

        if all(cell != "X" for row in player_board.board for cell in row):
            print("Computer has sunk all your ships! You lose.")
            return "game_over"  # Return "game_over" to indicate the game is over


def game():
    """
    Function to run the Battleships game.

    This function initializes the game, including setting up the player and computer boards,
    populating the boards with ships, and then running the game loop until one of the players wins
    or the user quits.

    The game loop alternates between the player's and computer's turns, allowing the player to make
    guesses on the computer's board and vice versa. The game continues until all ships of one player
    are sunk or the user chooses to quit the game.

    The function displays information about the game, including the board size, player's name,
    and instructions for making guesses. It also handles input validation to ensure the player
    enters valid guesses.
    """
    while True:
        size = 4
        num_ships = 3

        player_board = Board(size, num_ships)
        computer_board = Board(size, num_ships)

        # Populate both player's and computer's boards
        populate_board(player_board, num_ships)
        populate_board(computer_board, num_ships)

        # Hide ships on computer's board
        hidden_computer_board = computer_board.hide_ship()

        # Project 3 Scope video
        print("-" * 35)
        print("Welcome to Battleships")
        print(f"Board Size: {size} * {size}.")
        print(f"Number of ships: {num_ships}.")
        print("Top left corner is row: 0, column: 0")
        player_name = input("Enter your name: \n")
        print("-" * 35)

        print("\nComputer's Board:")
        for row in hidden_computer_board:
            print(" ".join(row))

        print(f"\n{player_name}'s Board:")
        player_board.print()
        print()  # Add an empty line here

        # Run the game loop
        game_result = game_loop(player_board, computer_board, size, player_name)

        # Check if the game is over due to sinking ships
        if game_result == "game_over":
            # Prompt for replay only if the game is ended by sinking ships
            replay = input("Do you want to play again? (y/n): ")
            if replay.lower() != 'y':
                print("Thanks for playing! Goodbye.")
                break  # Break out of the outer loop to end the game
        elif game_result == "quit":
            print("Thanks for playing! Goodbye.")
            break  # Break out of the outer loop to end the game 


game()
