def print_board(board):
    symbols = { -1: "X", 1: "O", 0: " " }
    print("\nTabuleiro:")
    for row in board:
        print("| " + " | ".join(symbols[cell] for cell in row) + " |")
    print()

def next_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return None 

def main():
    board = [
        [-1, 1, 1],
        [-1, -1, 0],
        [0, 1, 0]
    ]
    
    print_board(board)
    
    move = next_move(board)
    if move:
        print(f"Próxima jogada sugerida: linha {move[0]}, coluna {move[1]}")
    else:
        print("Tabuleiro completo, nenhuma jogada disponível.")

if __name__ == "__main__":
    main()
