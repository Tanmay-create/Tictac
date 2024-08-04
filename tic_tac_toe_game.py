import sys  # Import necessary libraries
import random  # Import necessary libraries

print(sys.version)  # Print Python version

# Constants
PLAYER_MARK = "X"
COMPUTER_MARK = "O"
EMPTY_CELL = " "

# Function to display the game board
def display_board(board):
    """Display the current game board state"""
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

# Function to handle user input
def user_input(board, position, mark):
    """Update the board with user's move"""
    if board[position] == EMPTY_CELL:
        board[position] = mark  # Single Responsibility Principle
    else:
        print("Invalid Input")  # Handle invalid input gracefully

# Function to make computer decision
def computer_decision(board, mark):
    """Computer randomly chooses an available position"""
    available_positions = [i for i, x in enumerate(board) if x == EMPTY_CELL]  # List Comprehension
    position = random.choice(available_positions)
    board[position] = mark  # Single Responsibility Principle

# Function to check for winning criteria
def check_winner(board, mark):
    """Check if the given mark has won"""
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal win conditions
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical win conditions
        (0, 4, 8), (2, 4, 6)              # Diagonal win conditions
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True  # Return early if a winning condition is met
    return False

# Function to handle the game logic
def tic_tac_toe_game():
    """Main function to run the Tic Tac Toe game"""
    board = [EMPTY_CELL for _ in range(9)]  # Initialize the game board using List Comprehension
    print("Welcome to Tic Tac Toe")  # User-friendly prompt
    display_board(board)  # Display the initial empty board

    while True:  # Game loop
        # User move
        try:
            user_pos = int(input("Enter your position (0-8): "))  # Input validation
            if user_pos < 0 or user_pos > 8:
                raise ValueError  # Raise error for invalid input
        except ValueError:
            print("Invalid input, please enter a number between 0 and 8.")
            continue

        user_input(board, user_pos, PLAYER_MARK)  # Process user move
        display_board(board)  # Display board after user move

        # Check if user won
        if check_winner(board, PLAYER_MARK):
            print("You won!")  # User-friendly output
            break

        # Check for tie
        if EMPTY_CELL not in board:
            print("It's a tie!")  # User-friendly output
            break

        # Computer move
        computer_decision(board, COMPUTER_MARK)  # Process computer move
        display_board(board)  # Display board after computer move

        # Check if computer won
        if check_winner(board, COMPUTER_MARK):
            print("Computer won!")  # User-friendly output
            break

# Main loop to run multiple games
if __name__ == "__main__":  # Entry point of the program
    while True:
        tic_tac_toe_game()  # Start a game
        play_again = input("Do you want to play again? (y/n): ").lower()  # Ask user if they want to play again
        if play_again != 'y':
            print("Thanks for playing!")  # User-friendly output
            break  # Exit the loop and end the program
