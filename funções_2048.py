import os
import random


def clear_screen():
    """
    Clears the console screen, works on both Windows and Unix-like systems.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_board():
    """
    Initializes the 4x4 game board of 2048 with two random values.
    
    Returns:
        list: A 2D list representing the board.
    """
    # Creates a 4x4 matrix filled with zeros to represent the empty board.
    board = [[0] * 4 for _ in range(4)]
    
    # Adds two random values (2 or 4) to the board.
    add_random_tile(board)
    add_random_tile(board)
    
    return board


def add_random_tile(board):
    """
    Adds a new value (2 or 4 with different probabilities) to a random empty position on the board.

    Args:
        board (list): The game board represented as a 2D list.
    """
    # Finds the empty cells on the board (cells with value 0).
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    
    if empty_cells:
        # Chooses a random empty cell.
        i, j = random.choice(empty_cells)
        
        # Sets the cell value to 2 (90% chance) or 4 (10% chance).
        board[i][j] = 2 if random.random() < 0.9 else 4


def print_colored_board(board):
    """
    Prints the colored 2048 board on the console.

    Args:
        board (list): The game board represented as a 2D list.
    """
    clear_screen()
    board_size = len(board)
    cell_width = 6

    title = "\033[1;36m2048 Game\033[0m"
    total_width = board_size * (cell_width + 4)
    title_padding = (total_width - len(title)) // 2

    # Prints the upper lines of the board.
    print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
    print(f"\033[1;37m|{' ' * (title_padding - 1)}{title}{' ' * (title_padding - 1 + len(title) % 2)}|\033[0m")

    for i in range(board_size):
        # Prints the intermediate lines of the board.
        print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
        for j in range(board_size):
            cell_value = board[i][j]
            cell_str = str(cell_value) if cell_value != 0 else " "

            if cell_value == 0:
                cell_color = "\033[0m"
            elif len(str(cell_value)) == 1:
                cell_color = "\033[1;37m"
            elif len(str(cell_value)) == 2:
                cell_color = "\033[1;34m"
            elif len(str(cell_value)) == 3:
                cell_color = "\033[1;32m"
            elif len(str(cell_value)) == 4:
                cell_color = "\033[1;31m"

            padding_left = " " * ((cell_width - len(cell_str)) // 2)
            padding_right = " " * (cell_width - len(cell_str) - len(padding_left))

            # Prints each cell of the board with the appropriate color and spacing.
            print(f"\033[1;37m|{padding_left}{cell_color}{cell_str}{padding_right}\033[0m", end="")
        # Prints the lower lines of the board.
        print("\033[1;37m|\033[0m")
    print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
    print("\n")


def move_left(board):
    """
    Moves the tiles on the board to the left, merging those that are equal while moving.
    
    Args:
        board (list): The game board represented as a 2D list.

    Returns:
        tuple: A tuple containing a boolean indicating if there was a movement and the total score of the merge.
    """
    moved = False
    total_score = 0
    for row in board:
        initial_row = row.copy()
        
        # Calls the merge_tiles function to merge the tiles in the row.
        merged_row, merge_score = merge_tiles(row)
        
        row[:] = merged_row
        
        # Checks if there was movement in the row.
        if row != initial_row:
            moved = True
        
        # Updates the total score with the merge score.
        total_score += merge_score  
    return moved, total_score  


def move_right(board):
    """
    Moves the tiles on the board to the right, merging those that are equal while moving.
    
    Args:
        board (list): The game board represented as a 2D list.

    Returns:
        tuple: A tuple containing a boolean indicating if there was a movement and the total score of the merge.
    """
    moved = False
    total_score = 0
    for row in board:
        initial_row = row.copy()
        
        # Reverses the order of the tiles in the row before calling merge_tiles.
        merged_row, merge_score = merge_tiles(row[::-1])
        
        row[:] = merged_row[::-1]
        
         # Checks if there was movement in the row.
        if row != initial_row:
            moved = True
            
        # Updates the total score with the merge score.
        total_score += merge_score
    return moved, total_score


def move_up(board):
    """
    Moves the tiles on the board upward, merging those that are equal while moving.
    
    Args:
        board (list): The game board represented as a 2D list.

    Returns:
        tuple: A tuple containing a boolean indicating if there was a movement and the total score of the merge.
    """
    moved = False
    total_score = 0
    for col in range(4):
        column = [board[row][col] for row in range(4)]
        initial_column = column.copy()
        
        # Calls the merge_tiles function to merge the tiles in the column.
        merged_column, merge_score = merge_tiles(column)
        
        for row in range(4):
            board[row][col] = merged_column[row]
        
        # Checks if there was movement in the column.
        if any(board[row][col] != initial_column[row] for row in range(4)):
            moved = True
        
        # Updates the total score with the merge score.
        total_score += merge_score
    return moved, total_score


def move_down(board):
    """
    Moves the tiles on the board downward, merging those that are equal while moving.
    
    Args:
        board (list): The game board represented as a 2D list.

    Returns:
        tuple: A tuple containing a boolean indicating if there was a movement and the total score of the merge.
    """
    moved = False
    total_score = 0
    for col in range(4):
        column = [board[row][col] for row in range(3, -1, -1)]
        initial_column = column.copy()
        
        # Calls the merge_tiles function to merge the tiles in the column.
        merged_column, merge_score = merge_tiles(column)
        
        for row in range(3, -1, -1):
            board[3 - row][col] = merged_column[row]
        
        # Checks if there was movement in the column.
        if any(board[row][col] != initial_column[3 - row] for row in range(4)):
            moved = True
        
        # Updates the total score with the merge score.
        total_score += merge_score
    return moved, total_score


def merge_tiles(line):
    """
    Merges the tiles in the line (or column) according to the rules of the 2048 game.
    
    Args:
        line (list): A list representing the line (or column) of the board.

    Returns:
        tuple: A tuple containing the merged line and the merge score.
    """
    merged_line = [0] * 4
    index = 0
    merge_score = 0  
    
    # Iterates over the tiles in the line.
    for tile in line:
        if tile != 0:
            if merged_line[index] == 0:
                merged_line[index] = tile
            elif merged_line[index] == tile:
                merged_line[index] *= 2
                merge_score += merged_line[index]
                index += 1
            else:
                index += 1
                merged_line[index] = tile
    
    return merged_line, merge_score  


def is_game_won(board, target_value=2048):
    """
    Checks if the player has won the game by reaching a target tile value.

    Args:
        board (list): The game board represented as a 2D list.
        target_value (int): The target value to win the game (default is 2048).

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Checks if there is any cell on the board with the target value.
    for row in board:
        if any(cell == target_value for cell in row):
            return True
    return False


def is_game_over(board):
    """
    Checks if the game has ended (no valid moves left).

    Args:
        board (list): The game board represented as a 2D list.

    Returns:
        bool: True if the game is over, False otherwise.
    """
    # Tests each of the four possible directions to check if there are still valid moves.
    for move_func in [move_left, move_right, move_up, move_down]:
        board_copy = [row[:] for row in board]
        if move_func(board_copy):
            return False
    return True

            
def input_direction():
    """
    Asks and returns the player's direction as input (W/A/S/D for movement, R for restart).

    Returns:
        str: The direction chosen by the player.
    """
    while True:
        direction = input("Enter direction (W/A/S/D): ").upper()
        if direction in ('W', 'A', 'S', 'D', 'R'):
            return direction
        else:
            print("Invalid input. Use W/A/S/D to move or R to restart.")


def stop_condition(board, score, move_count, game_history):
    """
    Determines if the game has ended and whether the player wants to play again.

    Args:
        board (list): The game board represented as a 2D list.
        score (int): The player's current score.
        move_count (int): The number of moves made.
        game_history (list): The list to store game history.

    Returns:
        bool: True if the player wants to stop playing, False if they want to continue.
    """
    if is_game_over(board):
        print("Game Over! You Lose!")
    elif is_game_won(board):
        print("Congratulations! You Win!")

    game_history.append({"score": score, "moves": move_count})  # Add game data to history
    
    restart = input("Do you want to play again? (Y/N): ").upper()
    while restart not in "YN":
        restart = input("Do you want to play again? (Y/N): ").upper()
    return restart == 'N'


def play_game(game_history):
    """
    The main game loop.

    Args:
        game_history (list): The list to store game history.

    Returns:
        bool: True if the player wants to restart the game, False if they want to quit.
    """
    board = initialize_board()
    score = 0
    move_count = 0

    while True:
        print_colored_board(board)
        print("Score:", score)
        print("Moves:", move_count)
        
        if is_game_won(board) or is_game_over(board):
            if stop_condition(board, score, move_count, game_history):
                break
            else:
                # Restart the game.
                board = initialize_board()
                score = 0
                move_count = 0
                continue
          
        direction = input_direction()
        moved, move_score = False, 0
        if direction == 'W':
            moved, move_score = move_up(board)
        elif direction == 'A':
            moved, move_score = move_left(board)
        elif direction == 'S':
            moved, move_score = move_down(board)
        elif direction == 'D':
            moved, move_score = move_right(board)
        elif direction == 'R':
            if stop_condition(board, score, move_count, game_history):
                break
            else:
                # Restart the game.
                board = initialize_board()
                score = 0
                move_count = 0
                continue

        if moved:
            add_random_tile(board)
            move_count += 1
            score += move_score
