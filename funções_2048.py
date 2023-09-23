import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board

def add_random_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4

def print_colored_board(board):
    clear_screen()
    board_size = len(board)
    cell_width = 6

    title = "\033[1;36m2048 Game\033[0m"
    total_width = board_size * (cell_width + 4)
    title_padding = (total_width - len(title)) // 2

    print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
    print(f"\033[1;37m|{' ' * (title_padding - 1)}{title}{' ' * (title_padding - 1 + len(title) % 2)}|\033[0m")

    for i in range(board_size):
        print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
        for j in range(board_size):
            cell_value = board[i][j]
            cell_str = str(cell_value) if cell_value != 0 else " "

            if cell_value == 0:
                cell_color = "\033[0m"
            elif 1 <= len(str(cell_value)) == 1:
                cell_color = "\033[1;37m"  
            elif 2 <= len(str(cell_value)) == 2:
                cell_color = "\033[1;34m" 
            elif 3 <= len(str(cell_value)) == 3:
                cell_color = "\033[1;32m" 
            elif 4 <= len(str(cell_value)) == 4:
                cell_color = "\033[1;31m"  

            padding_left = " " * ((cell_width - len(cell_str)) // 2)
            padding_right = " " * (cell_width - len(cell_str) - len(padding_left))

            print(f"\033[1;37m|{padding_left}{cell_color}{cell_str}{padding_right}\033[0m", end="")
        print("\033[1;37m|\033[0m")
    print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
    print("\n")

def move_left(board):
    moved = False
    total_score = 0
    for row in board:
        initial_row = row.copy()
        merged_row, merge_score = merge_tiles(row)
        row[:] = merged_row
        if row != initial_row:
            moved = True
        total_score += merge_score  
    return moved, total_score  

def move_right(board):
    moved = False
    total_score = 0
    for row in board:
        initial_row = row.copy()
        merged_row, merge_score = merge_tiles(row[::-1])
        row[:] = merged_row[::-1]
        if row != initial_row:
            moved = True
        total_score += merge_score
    return moved, total_score

def move_up(board):
    moved = False
    total_score = 0
    for col in range(4):
        column = [board[row][col] for row in range(4)]
        initial_column = column.copy()
        merged_column, merge_score = merge_tiles(column)
        for row in range(4):
            board[row][col] = merged_column[row]
        if any(board[row][col] != initial_column[row] for row in range(4)):
            moved = True
        total_score += merge_score
    return moved, total_score

def move_down(board):
    moved = False
    total_score = 0
    for col in range(4):
        column = [board[row][col] for row in range(3, -1, -1)]
        initial_column = column.copy()
        merged_column, merge_score = merge_tiles(column)
        for row in range(3, -1, -1):
            board[3 - row][col] = merged_column[row]
        if any(board[row][col] != initial_column[3 - row] for row in range(4)):
            moved = True
        total_score += merge_score
    return moved, total_score

def merge_tiles(line):
    merged_line = [0] * 4
    index = 0
    merge_score = 0  
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
    for row in board:
        if any(cell == target_value for cell in row):
            return True
    return False

def is_game_over(board):
    for move_func in [move_left, move_right, move_up, move_down]:
        board_copy = [row[:] for row in board]
        if move_func(board_copy):
            return False
    return True

def reset_board(board):
    for i in range(4):
        for j in range(4):
            board[i][j] = 0
            
def input_direction():
    while True:
        direction = input("Enter direction (W/A/S/D): ").upper()
        if direction in ('W', 'A', 'S', 'D', 'R'):
            return direction
        else:
            print("Invalid input. Use W/A/S/D to move or R to restart.")

def stop_condition(board):
    print("Game Over! You Lose!" if is_game_over(board) else "Congratulations! You Win!")
    restart = input("Do you want to play again? (Y/N): ").upper()
    while restart not in "YN":
        restart = input("Do you want to play again? (Y/N): ").upper()
    return restart == 'N'

def play_game():
    board = initialize_board()
    score = 0
    move_count = 0
    score_history = []
    move_count_history = []

    while True:
        print_colored_board(board)
        print("Score:", score)
        print("Moves:", move_count)
        
        if is_game_won(board) or is_game_over(board):
            if stop_condition(board):
                break
            else:
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
            return True  

        if moved:
            add_random_tile(board)
            move_count += 1
            score += move_score
            score_history.append(score)
            move_count_history.append(move_count)

    return False

def main():
    while True:
        should_restart = play_game()
        if not should_restart:
            break
