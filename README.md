# 2048 Game
## Descrição
Este é um jogo 2048 implementado em Python, onde o objetivo é combinar blocos com números iguais para alcançar o bloco 2048.

## Funcionalidades
- **clear_screen():** Limpa a tela do console.
- **initialize_board():** Inicializa o tabuleiro do jogo 4x4 com dois valores aleatórios.
- **add_random_tile(board):** Adiciona um novo valor (2 ou 4) a uma posição aleatória vazia no tabuleiro.
- **print_colored_board(board):** Imprime o tabuleiro 2048 colorido no console.
- **move_left(board):** Move as peças no tabuleiro para a esquerda, mesclando aquelas que são iguais enquanto se movem.
- **move_right(board):** Move as peças no tabuleiro para a direita, mesclando aquelas que são iguais enquanto se movem.
- **move_up(board):** Move as peças no tabuleiro para cima, mesclando aquelas que são iguais enquanto se movem.
- **move_down(board):** Move as peças no tabuleiro para baixo, mesclando aquelas que são iguais enquanto se movem.
- **merge_tiles(line):** Mescla as peças na linha (ou coluna) de acordo com as regras do jogo 2048.
- **is_game_won(board, target_value=2048):** Verifica se o jogador ganhou o jogo alcançando um valor específico.
- **is_game_over(board):** Verifica se o jogo acabou (sem movimentos válidos restantes).
- **input_direction():** Pergunta e retorna a direção escolhida pelo jogador como entrada (W/A/S/D para movimento, R para reiniciar).
- **stop_condition(board, score, move_count, game_history):** Determina se o jogo acabou e se o jogador quer jogar novamente.
- **play_game(game_history):** O loop principal do jogo.
- **main():** A função principal que inicia o jogo 2048.
## Pré-requisitos
- Python 3.x instalado.
## Instalação
1. Clone este repositório para o seu computador:<br>
```$ git clone https://github.com/seu_usuario/seu_repositorio.git```
2. Navegue até o diretório do projeto:<br>
```$ cd seu_repositorio```
3. Execute o jogo:<br>
```$ python main.py```
## Uso
- Execute o jogo e siga as instruções fornecidas no console.
- Use as teclas W, A, S, D para mover as peças para cima, esquerda, baixo e direita, respectivamente.
- Pressione R para reiniciar o jogo a qualquer momento.
## Contribuição
Contribuições são bem-vindas! Se você encontrar um problema ou tiver sugestões para melhorar o jogo, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License.

## Agradecimentos
Aos criadores do jogo 2048 por nos fornecerem uma divertida forma de passar o tempo.
A todos os colaboradores que ajudaram a melhorar este jogo.
## Contato
- Para mais informações ou perguntas, entre em contato com lucas.damasceno.dev@gmail.com.
