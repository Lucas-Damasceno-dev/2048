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

def print_board(board):
    clear_screen()
    for row in board:
        print(' | '.join(str(cell) if cell != 0 else '.' for cell in row))
        print('-' * 13)

def move_left(board):
    moved = False
    for row in board:
        initial_row = row.copy()
        row[:] = merge_tiles(row)
        if row != initial_row:
            moved = True
    return moved

def move_right(board):
    moved = False
    for row in board:
        initial_row = row.copy()
        row[:] = merge_tiles(row[::-1])[::-1]
        if row != initial_row:
            moved = True
    return moved

def move_up(board):
    moved = False
    for col in range(4):
        column = [board[row][col] for row in range(4)]
        initial_column = column.copy()
        merged_column = merge_tiles(column)
        for row in range(4):
            board[row][col] = merged_column[row]
        if any(board[row][col] != initial_column[row] for row in range(4)):
            moved = True
    return moved

def move_down(board):
    moved = False
    for col in range(4):
        column = [board[row][col] for row in range(3, -1, -1)]
        initial_column = column.copy()
        merged_column = merge_tiles(column)
        for row in range(3, -1, -1):
            board[3 - row][col] = merged_column[row]
        if any(board[row][col] != initial_column[3 - row] for row in range(4)):
            moved = True
    return moved

def merge_tiles(line):
    merged_line = [0] * 4
    index = 0
    for tile in line:
        if tile != 0:
            if merged_line[index] == 0:
                merged_line[index] = tile
            elif merged_line[index] == tile:
                merged_line[index] *= 2
                index += 1
            else:
                index += 1
                merged_line[index] = tile
    return merged_line

def is_game_over(board):
    # Verifica se há movimentos possíveis em todas as direções
    for move_func in [move_left, move_right, move_up, move_down]:
        board_copy = [row[:] for row in board]
        if move_func(board_copy):
            return False
    return True

def main():
    board = initialize_board()
    while True:
        print_board(board)
        if is_game_over(board):
            print("Game Over!")
            break
        direction = input("Enter direction (W/A/S/D): ").upper()
        moved = False
        if direction == 'W':
            moved = move_up(board)
        elif direction == 'A':
            moved = move_left(board)
        elif direction == 'S':
            moved = move_down(board)
        elif direction == 'D':
            moved = move_right(board)
        else:
            print("Invalid input. Use W/A/S/D to move.")
        
        if moved:
            add_random_tile(board)

if __name__ == "__main__":
    main()

