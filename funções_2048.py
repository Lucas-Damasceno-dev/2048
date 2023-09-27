import os
import random


def clear_screen():
    """
    Limpa a tela do console, funcionando em sistemas Windows e Unix-like.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize_board():
    """
    Inicializa o tabuleiro 4x4 do jogo 2048 com dois valores aleatórios.
    
    Retorna:
        list: Uma lista 2D representando o tabuleiro.
    """
    # Cria uma matriz 4x4 preenchida com zeros para representar o tabuleiro vazio.
    board = [[0] * 4 for _ in range(4)]
    
    # Adiciona dois valores aleatórios (2 ou 4) ao tabuleiro.
    add_random_tile(board)
    add_random_tile(board)
    
    return board


def add_random_tile(board):
    """
    Adiciona um novo valor (2 ou 4 com probabilidades diferentes) em uma posição aleatória vazia no tabuleiro.

    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.
    """
    # Encontra as células vazias no tabuleiro (células com valor 0).
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    
    if empty_cells:
        # Escolhe uma célula vazia aleatória.
        i, j = random.choice(empty_cells)
        
        # Define o valor da célula como 2 (90% de chance) ou 4 (10% de chance).
        board[i][j] = 1024 if random.random() < 0.9 else 1024


def print_colored_board(board):
    """
    Imprime o tabuleiro 2048 colorido no console.

    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.
    """
    clear_screen()
    board_size = len(board)
    cell_width = 6

    title = "\033[1;36m2048 Game\033[0m"
    total_width = board_size * (cell_width + 4)
    title_padding = (total_width - len(title)) // 2

    # Imprime as linhas superiores do tabuleiro.
    print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
    print(f"\033[1;37m|{' ' * (title_padding - 1)}{title}{' ' * (title_padding - 1 + len(title) % 2)}|\033[0m")

    for i in range(board_size):
        # Imprime as linhas intermediárias do tabuleiro.
        print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
        for j in range(board_size):
            cell_value = board[i][j]
            cell_str = str(cell_value) if cell_value != 0 else " "

            if cell_value == 0:
                cell_color = "\033[0m"
            elif 1 <= len(str(cell_value)) <= 2:
                cell_color = "\033[1;37m"  # Pinta os valores de apenas 1 digito de branco
            elif 3 <= len(str(cell_value)) <= 4:
                cell_color = "\033[1;34m" # Pinta os valores de apenas 2 digitos de azul
            elif 5 <= len(str(cell_value)) <= 6:
                cell_color = "\033[1;32m" # Pinta os valores de apenas 3 digitos de verde
            elif 7 <= len(str(cell_value)):
                cell_color = "\033[1;31m"  # Pinta os valores de apenas 4 digitos de vermelho

            padding_left = " " * ((cell_width - len(cell_str)) // 2)
            padding_right = " " * (cell_width - len(cell_str) - len(padding_left))

            # Imprime cada célula do tabuleiro com cor e espaçamento adequados.
            print(f"\033[1;37m|{padding_left}{cell_color}{cell_str}{padding_right}\033[0m", end="")
        # Imprime as linhas inferiores do tabuleiro.
        print("\033[1;37m|\033[0m")
    print("\033[1;37m+" + "+".join(["-" * cell_width] * board_size) + "+\033[0m")
    print("\n")


def move_left(board):
    """
    Move as peças no tabuleiro para a esquerda, mesclando as que são iguais ao se mover.
    
    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.

    Returns:
        tuple: Uma tupla contendo um booleano que indica se houve movimento e a pontuação total da mesclagem.
    """
    moved = False
    total_score = 0
    for row in board:
        initial_row = row.copy()
        
        # Chama a função merge_tiles para mesclar as peças na linha.
        merged_row, merge_score = merge_tiles(row)
        
        row[:] = merged_row
        
        # Verifica se houve movimento na linha.
        if row != initial_row:
            moved = True
        
        # Atualiza a pontuação total com a pontuação da mesclagem.
        total_score += merge_score  
    return moved, total_score  


def move_right(board):
    """
    Move as peças no tabuleiro para a direita, mesclando as que são iguais ao se mover.
    
    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.

    Returns:
        tuple: Uma tupla contendo um booleano que indica se houve movimento e a pontuação total da mesclagem.
    """
    moved = False
    total_score = 0
    for row in board:
        initial_row = row.copy()
        
        # Inverte a ordem das peças na linha antes de chamar merge_tiles.
        merged_row, merge_score = merge_tiles(row[::-1])
        
        row[:] = merged_row[::-1]
        
         # Verifica se houve movimento na linha.
        if row != initial_row:
            moved = True
            
        # Atualiza a pontuação total com a pontuação da mesclagem.
        total_score += merge_score
    return moved, total_score


def move_up(board):
    """
    Move as peças no tabuleiro para cima, mesclando as que são iguais ao se mover.
    
    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.

    Returns:
        tuple: Uma tupla contendo um booleano que indica se houve movimento e a pontuação total da mesclagem.
    """
    moved = False
    total_score = 0
    for col in range(4):
        column = [board[row][col] for row in range(4)]
        initial_column = column.copy()
        
        # Chama a função merge_tiles para mesclar as peças na coluna.
        merged_column, merge_score = merge_tiles(column)
        
        for row in range(4):
            board[row][col] = merged_column[row]
        
        # Verifica se houve movimento na coluna.
        if any(board[row][col] != initial_column[row] for row in range(4)):
            moved = True
        
        # Atualiza a pontuação total com a pontuação da mesclagem.
        total_score += merge_score
    return moved, total_score


def move_down(board):
    """
    Move as peças no tabuleiro para baixo, mesclando as que são iguais ao se mover.
    
    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.

    Returns:
        tuple: Uma tupla contendo um booleano que indica se houve movimento e a pontuação total da mesclagem.
    """
    moved = False
    total_score = 0
    for col in range(4):
        column = [board[row][col] for row in range(3, -1, -1)]
        initial_column = column.copy()
        
        # Chama a função merge_tiles para mesclar as peças na coluna.
        merged_column, merge_score = merge_tiles(column)
        
        for row in range(3, -1, -1):
            board[3 - row][col] = merged_column[row]
        
        # Verifica se houve movimento na coluna.
        if any(board[row][col] != initial_column[3 - row] for row in range(4)):
            moved = True
        
        # Atualiza a pontuação total com a pontuação da mesclagem.
        total_score += merge_score
    return moved, total_score


def merge_tiles(line):
    """
    Mescla as peças na linha (ou coluna) de acordo com as regras do jogo 2048.
    
    Args:
        line (list): Uma lista representando a linha (ou coluna) do tabuleiro.

    Returns:
        tuple: Uma tupla contendo a linha mesclada e a pontuação da mesclagem.
    """
    merged_line = [0] * 4
    index = 0
    merge_score = 0  
    
    # Itera sobre as peças na linha.
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
    Verifica se o jogador ganhou o jogo alcançando um valor de peça alvo.

    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.
        target_value (int): O valor alvo para ganhar o jogo (padrão é 2048).

    Returns:
        bool: True se o jogador ganhou, False caso contrário.
    """
    # Verifica se há alguma célula no tabuleiro com o valor alvo.
    for row in board:
        if any(cell == target_value for cell in row):
            return True
    return False


def is_game_over(board):
    """
    Verifica se o jogo chegou ao fim (sem movimentos válidos restantes).

    Args:
        board (list): O tabuleiro do jogo representado como uma lista 2D.

    Returns:
        bool: True se o jogo acabou, False caso contrário.
    """
    # Testa cada uma das quatro direções possíveis para verificar se ainda há movimentos válidos.
    for move_func in [move_left, move_right, move_up, move_down]:
        board_copy = [row[:] for row in board]
        if move_func(board_copy):
            return False
    return True

            
def input_direction():
    """
    Solicita e retorna a direção do jogador como entrada (W/A/S/D para movimento, R para reiniciar).

    Returns:
        str: A direção escolhida pelo jogador.
    """
    while True:
        direction = input("Enter direction (W/A/S/D): ").upper()
        if direction in ('W', 'A', 'S', 'D', 'R'):
            return direction
        else:
            print("Invalid input. Use W/A/S/D to move or R to restart.")


def stop_condition(board, score, move_count, game_history=None):
    """
    Determine if the game has ended and whether the player wants to play again.

    Args:
        board (list): The game board represented as a 2D list.
        score (int): The player's current score.
        move_count (int): The number of moves made.
        game_history (list, optional): The list to store game history.

    Returns:
        bool: True if the player wants to stop playing, False if they want to continue.
    """
    print("Game Over! You Lose!" if is_game_over(board) else "Congratulations! You Win!")
    
    if game_history is not None:
        game_history.append({"score": score, "moves": move_count})  # Add game data to history
    
    restart = input("Do you want to play again? (Y/N): ").upper()
    while restart not in "YN":
        restart = input("Do you want to play again? (Y/N): ").upper()
    return restart == 'N'


def stop_condition(board, score, move_count, game_history):
    """
    Determine if the game has ended and whether the player wants to play again.

    Args:
        board (list): The game board represented as a 2D list.
        score (int): The player's current score.
        move_count (int): The number of moves made.
        game_history (list): The list to store game history.

    Returns:
        bool: True if the player wants to stop playing, False if they want to continue.
    """
    print("Game Over! You Lose!" if is_game_over(board) else "Congratulations! You Win!")
    
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


def main():
    """
    The main function that starts the 2048 game.

    The function continues the game execution until the player chooses not to restart.
    """
    game_history = []  # Initialize the game history list
    
    while True:
        should_restart = play_game(game_history)
        if not should_restart:
            break

    # Display the game history
    print("Game History:")
    for i, game_data in enumerate(game_history, start=1):
        print(f"Game {i}: Score = {game_data['score']}, Moves = {game_data['moves']}")
    