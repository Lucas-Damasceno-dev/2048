from funções_2048 import play_game

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
    
    
if __name__ == "__main__":
    main()
