import random


def create_board():
    board4x4 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return board4x4


def create_starting_blocks(board4x4):
    for _ in range(2):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if board4x4[i][j] == 0]
        if empty_positions:
            i, j = random.choice(empty_positions)
            board4x4[i][j] = random.choice([2, 4])
    for row in  board4x4:
        print(row)
    return board4x4


def possible_movement(board4x4):
    while True:
        direction = str(input('[w:up] [s:down] [a:left] [d:right]\n'
                            'Enter the desired direction: ')).strip().lower()
        match direction:
            case 'w':
                
            case 's':

            case 'a':
                
            case 'd':

            case _:
                print("Invalid direction! Please enter 'w', 's', 'a', or 'd'.")


    

board = create_board()
create_starting_blocks(board)
possible_movement(board)
            
            

